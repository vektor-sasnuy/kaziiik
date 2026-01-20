from django.db import models
from cars.models import Cars
from atvs.models import Atvs
from mopeds.models import Moped
from motocycles.models import Motocycles
import random


class Case(models.Model):
    """Модель для кейсів з транспортом"""
    RARITY_CHOICES = (
        ('common', 'Звичайний'),
        ('rare', 'Рідкісний'),
        ('epic', 'Епічний'),
        ('legendary', 'Легендарний'),
    )
    
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES, default='common')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='cases/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_rarity_display()})"
    
    class Meta:
        verbose_name_plural = "Cases"
        ordering = ['-created_at']


class CaseReward(models.Model):
    """Модель для нагород в кейсах"""
    VEHICLE_TYPES = (
        ('car', 'Car'),
        ('atv', 'ATV'),
        ('moped', 'Moped'),
        ('motocycle', 'Motocycle'),
    )
    
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='rewards')
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    
    # Foreign keys до кожного типу транспорту
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, null=True, blank=True)
    atv = models.ForeignKey(Atvs, on_delete=models.CASCADE, null=True, blank=True)
    moped = models.ForeignKey(Moped, on_delete=models.CASCADE, null=True, blank=True)
    motocycle = models.ForeignKey(Motocycles, on_delete=models.CASCADE, null=True, blank=True)
    
    # Вероятность випадения (0-100)
    probability = models.IntegerField(default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        vehicle = self.get_vehicle()
        return f"{self.case.name} -> {vehicle.name if vehicle else 'Unknown'}"
    
    def get_vehicle(self):
        """Получить объект транспорта"""
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
        verbose_name_plural = "Case Rewards"


class OpenedCase(models.Model):
    """Модель для историї відкритих кейсів"""
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='opened_cases')
    reward = models.ForeignKey(CaseReward, on_delete=models.SET_NULL, null=True, blank=True)
    opened_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        vehicle = self.reward.get_vehicle() if self.reward else None
        return f"{self.case.name} -> {vehicle.name if vehicle else 'No reward'}"
    
    class Meta:
        verbose_name_plural = "Opened Cases"
        ordering = ['-opened_at']
    
    @staticmethod
    def get_random_reward(case):
        """Обрати випадкову нагороду з кейса на основі вероятностей"""
        rewards = case.rewards.all()
        if not rewards.exists():
            return None
        
        # Обчислити загальну вероятність
        total_probability = sum(r.probability for r in rewards)
        
        # Сгенерировать случайное число
        random_num = random.randint(1, total_probability)
        
        # Найти нагороду
        cumulative = 0
        for reward in rewards:
            cumulative += reward.probability
            if random_num <= cumulative:
                return reward
        
        return rewards.last()
