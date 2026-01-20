from django.db import models
from cars.models import Cars
from atvs.models import Atvs
from mopeds.models import Moped
from motocycles.models import Motocycles


class Garage(models.Model):
    name = models.CharField(max_length=100, default="My Garage")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Garages"


class GarageItem(models.Model):
    VEHICLE_TYPES = (
        ('car', 'Car'),
        ('atv', 'ATV'),
        ('moped', 'Moped'),
        ('motocycle', 'Motocycle'),
    )
    
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, related_name='items')
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    
    # Foreign keys to each vehicle type (use null=True since only one will be populated)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, null=True, blank=True)
    atv = models.ForeignKey(Atvs, on_delete=models.CASCADE, null=True, blank=True)
    moped = models.ForeignKey(Moped, on_delete=models.CASCADE, null=True, blank=True)
    motocycle = models.ForeignKey(Motocycles, on_delete=models.CASCADE, null=True, blank=True)
    
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.vehicle_type == 'car':
            return f"{self.car.name}"
        elif self.vehicle_type == 'atv':
            return f"{self.atv.name}"
        elif self.vehicle_type == 'moped':
            return f"{self.moped.name}"
        elif self.vehicle_type == 'motocycle':
            return f"{self.motocycle.name}"
        return "Unknown"
    
    def get_vehicle(self):
        if self.vehicle_type == 'car':
            return self.car
        elif self.vehicle_type == 'atv':
            return self.atv
        elif self.vehicle_type == 'moped':
            return self.moped
        elif self.vehicle_type == 'motocycle':
            return self.motocycle
        return None
    
    class Meta:
        verbose_name_plural = "Garage Items"
