import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.admin import site
from cases.models import Case, CaseReward, OpenedCase

print("✅ Перевірка реєстрації адміністраторських моделей\n")

registered_models = [model.__name__ for model, admin in site._registry.items()]

print("📋 Зареєстровані в адмін-панелі моделі Cases app:")
if 'Case' in registered_models:
    print("   ✅ Case")
else:
    print("   ❌ Case")

if 'CaseReward' in registered_models:
    print("   ✅ CaseReward")
else:
    print("   ❌ CaseReward")

if 'OpenedCase' in registered_models:
    print("   ✅ OpenedCase")
else:
    print("   ❌ OpenedCase")

print("\n📊 Статистика:")
print(f"   Всього кейсів: {Case.objects.count()}")
print(f"   Всього нагород: {CaseReward.objects.count()}")
print(f"   Розкрито: {OpenedCase.objects.count()}")
