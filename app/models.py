from django.db import models

from django.db import models

class Metric(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    consumption_kwh = models.FloatField()
    solar_generation_kwh = models.FloatField(default=0.0)
    estimated_cost_brl = models.FloatField()
    def __str__(self):
        return f"{self.timestamp.strftime('%H:%M:%S')} - {self.consumption_kwh} kWh"



class ConsumerUnit(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome / Razão Social")
    address = models.CharField(max_length=200, verbose_name="Endereço da Instalação")
    inverter_model = models.CharField(max_length=100, default="GoodWe GW5000D-NS", verbose_name="Modelo do Inversor")
    system_power_kwp = models.FloatField(default=5.0, verbose_name="Potência Instalada (kWp)")
    energy_tariff_brl = models.FloatField(default=0.85, verbose_name="Tarifa por kWh (R$)")

    def __str__(self):
        return f"{self.name} - {self.inverter_model}"
