from django.db import models
from django.db.models import CASCADE


class ConsumerUnit(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome / Razão Social")
    address = models.CharField(max_length=200, verbose_name="Endereço da Instalação")
    inverter_model = models.CharField(max_length=100, default="GoodWe GW5000D-NS", verbose_name="Modelo do Inversor")
    system_power_kwp = models.FloatField(default=5.0, verbose_name="Potência Instalada (kWp)")
    energy_tariff_brl = models.FloatField(default=0.85, verbose_name="Tarifa por kWh (R$)")

    def __str__(self):
        return f"{self.name} - {self.inverter_model}"


class EVCharger(models.Model):
    STATUS_CHOICES = [
        ('IDLE', 'Aguardando Veículo'),
        ('CHARGING', 'Carregando (Energia Solar)'),
        ('GRID_CHARGING', 'Carregando (Rede Elétrica)'),
        ('PAUSED', 'Pausado (Controle de Demanda)'),
    ]

    unit = models.ForeignKey(ConsumerUnit, on_delete=CASCADE, related_name="chargers", null=True, blank=True)
    charger_model = models.CharField(max_length=100, default="GoodWe HCA Series EV Charger")
    is_active = models.BooleanField(default=False)
    charging_power_kw = models.FloatField(default=7.4)  # Potência de carregamento (ex: 7.4 kW)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='IDLE')
    smart_charging_enabled = models.BooleanField(default=True, verbose_name="Automação / Priorizar Solar")

    def __str__(self):
        return f"{self.charger_model} - {self.get_status_display()}"

class Metric(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    consumption_kwh = models.FloatField()
    solar_generation_kwh = models.FloatField(default=0.0)
    ev_consumption_kwh = models.FloatField(default=0.0)
    estimated_cost_brl = models.FloatField()
    demand_alert = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.timestamp.strftime('%H:%M:%S')} - {self.consumption_kwh} kWh"