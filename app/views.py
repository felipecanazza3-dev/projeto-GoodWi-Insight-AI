
import os
import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from dotenv import load_dotenv
import google.generativeai as genai
from .models import Metric, ConsumerUnit, EVCharger

load_dotenv()
# Lembre-se de configurar a variável de ambiente GEMINI_API_KEY no seu ficheiro .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def home(request):
    return render(request, 'home.html')

def ia(request):
    return render(request, 'ia.html')

def grafico(request):
    return render(request, 'grafico.html')

def get_live_data(request):
    # Pega a unidade consumidora mais recente cadastrada ou cria uma padrão se não houver nenhuma
    unit = ConsumerUnit.objects.last()
    if not unit:
        unit = ConsumerUnit.objects.create(
            name='Felipe Alves',
            address='São Paulo, SP',
            inverter_model='GoodWe GW5000D-NS',
            system_power_kwp=5.0,
            energy_tariff_brl=0.85
        )

    # Simulação de geração solar e consumo da residência
    generation = round(random.uniform(8.0, 25.0), 2)
    base_consumption = round(random.uniform(10.0, 20.0), 2)

    # Verifica status do carregador de veículos elétricos (VE)
    charger, _ = EVCharger.objects.get_or_create(id=1)
    ev_consumption = 0.0

    # Lógica de Automação e Controle de Demanda
    if charger.is_active:
        if charger.smart_charging_enabled and generation < base_consumption:
            charger.status = 'PAUSED'
            ev_consumption = 0.0
        else:
            charger.status = 'CHARGING' if generation >= base_consumption else 'GRID_CHARGING'
            ev_consumption = charger.charging_power_kw
        charger.save()
    else:
        charger.status = 'IDLE'
        charger.save()

    total_consumption = round(base_consumption + ev_consumption, 2)

    # Cálculo real do custo utilizando a tarifa do perfil (R$) com o operador '*' corrigido
    cost = round(total_consumption * unit.energy_tariff_brl, 2)
    demand_alert = total_consumption > 35.0

    metric = Metric.objects.create(
        consumption_kwh=total_consumption,
        solar_generation_kwh=generation,
        ev_consumption_kwh=ev_consumption,
        estimated_cost_brl=cost,
        demand_alert=demand_alert
    )

    return JsonResponse({
        'timestamp': metric.timestamp.strftime('%H:%M:%S'),
        'consumption': metric.consumption_kwh,
        'generation': metric.solar_generation_kwh,
        'ev_consumption': metric.ev_consumption_kwh,
        'cost': metric.estimated_cost_brl,
        'tariff_used': unit.energy_tariff_brl,
        'alert': metric.demand_alert,
        'charger_status': charger.get_status_display(),
        'charger_active': charger.is_active
    })
def toggle_ev_charger(request):
    """ Endpoint para simular o ligar/desligar do carregador de VE GoodWe """
    if request.method == 'POST':
        charger, _ = EVCharger.objects.get_or_create(id=1)
        charger.is_active = not charger.is_active
        charger.save()
        return JsonResponse({'status': charger.is_active, 'charger_status': charger.get_status_display()})
    return JsonResponse({'error': 'Método não permitido'}, status=400)

def ask_gemini(request):
    if request.method == 'POST':
        user_prompt = request.POST.get('prompt', '')
        if not user_prompt:
            return JsonResponse({'reply': 'Por favor, envie uma pergunta válida.'})

        system_instruction = (
            "Você é o assistente virtual oficial da GoodWe. "
            "Sua função é tirar dúvidas técnicas e dar suporte sobre ecossistemas de energia solar GoodWe, "
            "inversores, baterias, carregadores de Veículos Elétricos (VE) GoodWe HCA, automação de consumo, "
            "controle de demanda e eficiência energética. "
            "Caso o usuário pergunte algo fora do escopo de energia solar, mobilidade elétrica ou ecossistema GoodWe, "
            "responda educadamente que seu foco é exclusivo em soluções GoodWe."
        )
        try:
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash",
                system_instruction=system_instruction
            )
            response = model.generate_content(user_prompt)
            return JsonResponse({'reply': response.text})
        except Exception as e:
            return JsonResponse({'reply': f"Erro ao processar mensagem: {str(e)}"})

    return JsonResponse({'reply': 'Método não permitido.'}, status=400)


def perfil(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        endereco = request.POST.get('address')
        inversor = request.POST.get('inverter_model')

        # Tratamento seguro para conversão de números
        potencia_str = request.POST.get('system_power_kwp', '5.0').replace(',', '.')
        tarifa_str = request.POST.get('energy_tariff_brl', '0.85').replace(',', '.')

        potencia = float(potencia_str) if potencia_str else 5.0
        tarifa = float(tarifa_str) if tarifa_str else 0.85

        # Cria SEMPRE um novo objeto no banco de dados SQLite
        ConsumerUnit.objects.create(
            name=nome,
            address=endereco,
            inverter_model=inversor,
            system_power_kwp=potencia,
            energy_tariff_brl=tarifa
        )
        return redirect('sistemas')

    return render(request, 'perfil.html')


def sus(request):
    return render(request,'sus.html')


def sistemas(request):
    filtro = ConsumerUnit.objects.all().order_by('-energy_tariff_brl')
    if request.method == 'POST':
        termo_busca = request.POST.get('busca', '')
        if termo_busca:
            filtro = ConsumerUnit.objects.filter(name__icontains=termo_busca).order_by('-energy_tariff_brl')

    context = {
        "filtro": filtro
    }
    return render(request, 'sistemas.html', context)

def remove_button(request):
    ConsumerUnit.objects.all().delete()
    return redirect('sistemas')

