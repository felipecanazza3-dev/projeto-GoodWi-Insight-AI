import random
import os
import google.generativeai as genai
from django.http import JsonResponse
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from .models import Metric, ConsumerUnit
from django.contrib import messages

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def home(request):
    return render(request, 'home.html')

def get_live_data(request):
    consumption = round(random.uniform(15.0, 45.0), 2)
    generation = round(random.uniform(5.0, 20.0), 2)
    cost = round(consumption * 0.75, 2)

    metric = Metric.objects.create(
        consumption_kwh=consumption,
        solar_generation_kwh=generation,
        estimated_cost_brl=cost
    )

    return JsonResponse({
        'timestamp': metric.timestamp.strftime('%H:%M:%S'),
        'consumption': metric.consumption_kwh,
        'generation': metric.solar_generation_kwh,
        'cost': metric.estimated_cost_brl,
        'alert': metric.consumption_kwh > 40.0
    })

def ia(request):

    return render(request,'ia.html')

def grafico(request):
    return render(request,'grafico.html')


def ask_gemini(request):
    if request.method == 'POST':
        user_prompt = request.POST.get('prompt', '')

        if not user_prompt:
            return JsonResponse({'reply': 'Por favor, envie uma pergunta válida.'})


        system_instruction = (
            "Você é o assistente virtual oficial da GoodWi / GoodWe. "
            "Sua ÚNICA função é responder dúvidas sobre produtos GoodWe (inversores solares, baterias, carregadores de veículos elétricos - VE), "
            "eficiência energética, energia solar e dados do gráfico de consumo do dashboard. "
            "Se o usuário perguntar algo fora deste contexto, responda gentilmente que seu foco exclusivo é auxiliar com soluções GoodWe e energia."
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
    unit, created = ConsumerUnit.objects.get_or_create(id=1, defaults={
        'name': 'Felipe Alves',
        'address': 'São Paulo, SP',
        'inverter_model': 'GoodWe GW5000D-NS',
        'system_power_kwp': 5.0,
        'energy_tariff_brl': 0.85
    })

    if request.method == 'POST':
        unit.name = request.POST.get('name')
        unit.address = request.POST.get('address')
        unit.inverter_model = request.POST.get('inverter_model')
        unit.system_power_kwp = request.POST.get('system_power_kwp')
        unit.energy_tariff_brl = request.POST.get('energy_tariff_brl')
        unit.save()

        messages.success(request, 'Dados da Unidade Consumidora atualizados com sucesso!')
        return redirect('perfil')

    return render(request, 'perfil.html', {'unit': unit})