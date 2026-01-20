import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from cars.models import Cars
from atvs.models import Atvs
from mopeds.models import Moped
from motocycles.models import Motocycles

# Очистити попередні дані
Cars.objects.all().delete()
Atvs.objects.all().delete()
Moped.objects.all().delete()
Motocycles.objects.all().delete()

print("🚗 Додаю машини...")
cars_data = [
    {'name': 'BMW 325i', 'body': 'Sedan', 'motor': 2.5, 'gear_type': True},
    {'name': 'Mazda RX-7', 'body': 'Coupe', 'motor': 1.3, 'gear_type': True},
    {'name': 'Toyota Camry', 'body': 'Sedan', 'motor': 2.5, 'gear_type': False},
    {'name': 'Honda Civic', 'body': 'Hatchback', 'motor': 1.8, 'gear_type': True},
    {'name': 'Ford Mustang', 'body': 'Coupe', 'motor': 5.0, 'gear_type': False},
    {'name': 'Audi A4', 'body': 'Sedan', 'motor': 2.0, 'gear_type': True},
    {'name': 'Mercedes-Benz C-Class', 'body': 'Sedan', 'motor': 2.0, 'gear_type': False},
    {'name': 'Volkswagen Golf', 'body': 'Hatchback', 'motor': 1.6, 'gear_type': True},
    {'name': 'Subaru Impreza', 'body': 'Sedan', 'motor': 2.0, 'gear_type': True},
    {'name': 'Porsche 911', 'body': 'Coupe', 'motor': 3.8, 'gear_type': True},
]

for car_data in cars_data:
    Cars.objects.create(**car_data)
    print(f"  ✅ {car_data['name']}")

print("\n🏍️  Додаю мотоцикли...")
motocycles_data = [
    {'name': 'Harley-Davidson Street 750', 'body': 'Cruiser', 'motor': 0.75, 'starter': True},
    {'name': 'Yamaha YZF-R1', 'body': 'Sport', 'motor': 1.0, 'starter': True},
    {'name': 'Honda PCX', 'body': 'Scooter', 'motor': 0.15, 'starter': False},
    {'name': 'Kawasaki Ninja H2', 'body': 'Sport', 'motor': 1.0, 'starter': True},
    {'name': 'Ducati Panigale V4', 'body': 'Sport', 'motor': 1.1, 'starter': True},
    {'name': 'BMW R 1250 GS', 'body': 'Adventure', 'motor': 1.25, 'starter': True},
    {'name': 'Royal Enfield Classic 350', 'body': 'Cruiser', 'motor': 0.35, 'starter': False},
    {'name': 'Vespa Primavera', 'body': 'Scooter', 'motor': 0.3, 'starter': False},
    {'name': 'derbi senda(limited edition2002)', 'body': 'Sport', 'motor': 0.05, 'starter': True},
    {'name': 'KTM 1290 Super Duke R', 'body': 'Naked', 'motor': 1.3, 'starter': True},
]

for moto_data in motocycles_data:
    Motocycles.objects.create(**moto_data)
    print(f"  ✅ {moto_data['name']}")

print("\n🛵 Додаю мопеди...")
mopeds_data = [
    {'name': 'Yamaha Jog', 'body': 'Scooter', 'motor': 0.05, 'starter': False},
    {'name': 'Honda LEAD', 'body': 'Scooter', 'motor': 0.1, 'starter': False},
    {'name': 'Suzuki Let\'s', 'body': 'Scooter', 'motor': 0.05, 'starter': False},
    {'name': 'Peugeot Vivacity', 'body': 'Scooter', 'motor': 0.1, 'starter': True},
    {'name': 'Aprilia SR 50', 'body': 'Sport', 'motor': 0.05, 'starter': True},
    {'name': 'Kymco Like 50', 'body': 'Scooter', 'motor': 0.05, 'starter': False},
    {'name': 'Piaggio ZIP 50', 'body': 'Scooter', 'motor': 0.05, 'starter': False},
    {'name': 'SYM Fiddle II', 'body': 'Scooter', 'motor': 0.1, 'starter': True},
]

for moped_data in mopeds_data:
    Moped.objects.create(**moped_data)
    print(f"  ✅ {moped_data['name']}")

print("\n🚙 Додаю ATV...")
atvs_data = [
    {'name': 'Yamaha Grizzly 700', 'body': 'All-Terrain', 'motor': 0.7, 'starter': True},
    {'name': 'Honda FourTrax Foreman 500', 'body': 'All-Terrain', 'motor': 0.5, 'starter': True},
    {'name': 'Suzuki KingQuad 750', 'body': 'All-Terrain', 'motor': 0.75, 'starter': True},
    {'name': 'Polaris Sportsman 850', 'body': 'All-Terrain', 'motor': 0.85, 'starter': True},
    {'name': 'Kawasaki Brute Force 750', 'body': 'All-Terrain', 'motor': 0.75, 'starter': True},
    {'name': 'Can-Am Outlander 650', 'body': 'All-Terrain', 'motor': 0.65, 'starter': True},
    {'name': 'Arctic Cat 450', 'body': 'All-Terrain', 'motor': 0.45, 'starter': True},
    {'name': 'Textron Off Road Alterra 570', 'body': 'All-Terrain', 'motor': 0.57, 'starter': True},
]

for atv_data in atvs_data:
    Atvs.objects.create(**atv_data)
    print(f"  ✅ {atv_data['name']}")

print("\n" + "="*50)
print("✅ База даних успішно заповнена!")
print("="*50)
print(f"\n📊 Статистика:")
print(f"   🚗 Машин: {Cars.objects.count()}")
print(f"   🏍️  Мотоциклів: {Motocycles.objects.count()}")
print(f"   🛵 Мопедів: {Moped.objects.count()}")
print(f"   🚙 ATV: {Atvs.objects.count()}")
print(f"   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"   📦 ВСЬОГО: {Cars.objects.count() + Motocycles.objects.count() + Moped.objects.count() + Atvs.objects.count()} засобів")
