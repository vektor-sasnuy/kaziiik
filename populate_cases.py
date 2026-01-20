"""
Скрипт для заповнення тестових даних для системи кейсів
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from cases.models import Case, CaseReward
from cars.models import Cars
from atvs.models import Atvs
from mopeds.models import Moped
from motocycles.models import Motocycles

# Очистити попередні кейси
Case.objects.all().delete()

# Створити тестові кейси

# 1. Звичайний кейс
common_case = Case.objects.create(
    name="Звичайний кейс",
    description="Базовий кейс для новачків",
    rarity="common",
    price=100
)

# 2. Рідкісний кейс
rare_case = Case.objects.create(
    name="Рідкісний кейс",
    description="Кейс з рідкісними транспортними засобами",
    rarity="rare",
    price=250
)

# 3. Епічний кейс
epic_case = Case.objects.create(
    name="Епічний кейс",
    description="Кейс з епічними награда",
    rarity="epic",
    price=500
)

# 4. Легендарний кейс
legendary_case = Case.objects.create(
    name="Легендарний кейс",
    description="Найрідший кейс в грі",
    rarity="legendary",
    price=1000
)

# Отримати всі транспортні засоби
cars = Cars.objects.all()
atvs = Atvs.objects.all()
mopeds = Moped.objects.all()
motocycles = Motocycles.objects.all()

# Додати нагороди до звичайного кейса
for i, car in enumerate(cars[:2]):
    CaseReward.objects.create(
        case=common_case,
        vehicle_type='car',
        car=car,
        probability=30 if i == 0 else 20
    )

for moped in mopeds[:2]:
    CaseReward.objects.create(
        case=common_case,
        vehicle_type='moped',
        moped=moped,
        probability=25
    )

# Додати нагороди до рідкісного кейса
for car in cars:
    CaseReward.objects.create(
        case=rare_case,
        vehicle_type='car',
        car=car,
        probability=25
    )

for atv in atvs:
    CaseReward.objects.create(
        case=rare_case,
        vehicle_type='atv',
        atv=atv,
        probability=25
    )

# Додати нагороди до епічного кейса
for i, motocycle in enumerate(motocycles):
    CaseReward.objects.create(
        case=epic_case,
        vehicle_type='motocycle',
        motocycle=motocycle,
        probability=35 if i == 0 else 30
    )

for car in cars:
    CaseReward.objects.create(
        case=epic_case,
        vehicle_type='car',
        car=car,
        probability=15
    )

# Додати нагороди до легендарного кейса
if motocycles.exists():
    best_motocycle = motocycles.first()
    CaseReward.objects.create(
        case=legendary_case,
        vehicle_type='motocycle',
        motocycle=best_motocycle,
        probability=50
    )

if cars.exists():
    best_car = cars.first()
    CaseReward.objects.create(
        case=legendary_case,
        vehicle_type='car',
        car=best_car,
        probability=50
    )

print("✅ Тестові кейси успішно створені!")
print(f"   - Звичайних кейсів: {common_case.rewards.count()}")
print(f"   - Рідкісних кейсів: {rare_case.rewards.count()}")
print(f"   - Епічних кейсів: {epic_case.rewards.count()}")
print(f"   - Легендарних кейсів: {legendary_case.rewards.count()}")
