import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from cases.models import Case, OpenedCase
from garage.models import Garage

print("🧪 Тестування системи кейсів...\n")

# Отримати перший кейс
case = Case.objects.first()
if not case:
    print("❌ Немає кейсів для тестування")
    exit(1)

print(f"📦 Обраний кейс: {case.name}")
print(f"   Рарність: {case.get_rarity_display()}")
print(f"   Нагород: {case.rewards.count()}\n")

# Отримати випадкову нагороду
print("🎲 Отримання випадкової нагороди...")
reward = OpenedCase.get_random_reward(case)

if reward:
    vehicle = reward.get_vehicle()
    print(f"✅ Отримана нагорода: {vehicle.name}")
    print(f"   Тип: {reward.get_vehicle_type_display()}")
    print(f"   Вероватність: {reward.probability}%\n")
    
    # Створити запис про відкриття
    print("📝 Запис про відкриття...")
    opened = OpenedCase.objects.create(case=case, reward=reward)
    print(f"✅ Кейс успішно відкрито! ID: {opened.id}\n")
    
    # Перевірити додавання в гараж
    garages = Garage.objects.all()
    if garages.exists():
        print(f"🚗 Гараж існує: {garages.first().name}")
        print(f"   Транспорт готовий бути доданим в гараж!")
    else:
        print("⚠️  Гаража немає, транспорт не буде доданий")
else:
    print("❌ Не вдалося отримати нагороду")

print(f"\n📊 Статистика:")
print(f"   Всього розкрито: {OpenedCase.objects.count()}")
