# Create your models here.
from django.db import models
from django.utils import timezone


class Type(models.Model):
    type_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.type_name


class Location(models.Model):
    endereco = models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.endereco


class Device(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=False, null=True)
    pte1 = models.PositiveBigIntegerField(default=0)
    pte2 = models.PositiveBigIntegerField(default=0)
    potencia = models.FloatField(default=3.14)
    chassis = models.CharField(max_length=50)
    slots = models.PositiveIntegerField(default=1)
    ports = models.PositiveIntegerField(default=1)
    endereco = models.ForeignKey(
        Location, on_delete=models.SET_NULL, blank=False, null=True
    )
    created_device = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name


class Local(models.Model):
    position = models.CharField(max_length=50)
    fila = models.CharField(max_length=50)
    bastidor = models.CharField(max_length=50)
    endereco = models.ForeignKey(
        Location, on_delete=models.SET_NULL, blank=False, null=True
    )
    device = models.ForeignKey(
        Device, on_delete=models.SET_NULL, blank=False, null=True
    )

    def __str__(self) -> str:
        return self.position


class Cable(models.Model):
    deviceA = models.ForeignKey(
        Device, on_delete=models.SET_NULL, null=True, related_name="device_A"
    )
    deviceB = models.ForeignKey(
        Device, on_delete=models.SET_NULL, null=True, related_name="device_B"
    )
    pontaA = models.CharField(max_length=50)
    pontaB = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    updated_cable = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Origem: {self.pontaA} || Destino: {self.pontaB}"
