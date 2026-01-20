import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from cases.models import Case, CaseReward, OpenedCase

print("✅ Система кейсів успішно завантажена!")
print(f"📦 Всього кейсів: {Case.objects.count()}")
print(f"🎁 Всього нагород: {CaseReward.objects.count()}")
print(f"📜 Розкрито кейсів: {OpenedCase.objects.count()}")
print("\n📋 Доступні кейси:")
for case in Case.objects.all():
    print(f"  - {case.name} ({case.rarity}) - {case.rewards.count()} нагород")
