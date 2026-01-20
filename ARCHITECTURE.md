# 🏗️ Архітектура системи кейсів

## 📊 Діаграма структури

```
Django Project (myproject)
│
├── cases/                    ← Новий app для системи кейсів
│   ├── models.py
│   │   ├── Case              ← Модель кейса
│   │   ├── CaseReward        ← Модель нагороди
│   │   └── OpenedCase        ← Модель історії
│   │
│   ├── views.py
│   │   ├── case_list()       ← Список кейсів
│   │   ├── case_detail()     ← Деталі кейса
│   │   ├── open_case()       ← Відкриття кейса
│   │   ├── open_case_animation() ← З анімацією
│   │   └── cases_history()   ← Історія
│   │
│   ├── admin.py
│   │   ├── CaseAdmin         ← Управління кейсами
│   │   ├── CaseRewardAdmin   ← Управління нагородами
│   │   └── OpenedCaseAdmin   ← Перегляд історії
│   │
│   ├── urls.py               ← URL маршрути
│   ├── forms.py              ← Форми
│   │
│   ├── templates/cases/
│   │   ├── case_list.html
│   │   ├── case_detail.html
│   │   ├── case_open_animation.html
│   │   └── history.html
│   │
│   ├── templatetags/
│   │   └── case_filters.py   ← Спеціальні фільтри
│   │
│   └── migrations/
│       └── 0001_initial.py
│
├── garage/                   ← Існуючий app
│   ├── models.py
│   │   ├── Garage            ← Гараж користувача
│   │   └── GarageItem        ← Предмет в гаражі
│   └── ...
│
├── cars/, atvs/, mopeds/, motocycles/ ← Типи транспорту
│   └── models.py
│       ├── Cars
│       ├── Atvs
│       ├── Moped
│       └── Motocycles
│
└── myproject/                ← Конфігурація
    └── settings.py           ← Додано 'cases' в INSTALLED_APPS
```

---

## 🔄 Потік даних

### Відкриття кейса

```
Користувач
    │
    ├─→ GET /cases/          → case_list view → Показати карточки кейсів
    │
    ├─→ GET /cases/<id>/     → case_detail view → Показати деталі
    │
    └─→ POST /cases/<id>/open/ → open_case view
        │
        ├─→ OpenedCase.get_random_reward(case)
        │   │
        │   ├─→ Отримати все нагороди кейса
        │   │
        │   ├─→ Обчислити вероватність (rand 1..total)
        │   │
        │   └─→ Повернути нагороду
        │
        ├─→ OpenedCase.objects.create(case=case, reward=reward)
        │   │
        │   └─→ Запис в базі даних
        │
        ├─→ GarageItem.objects.create(...)
        │   │
        │   └─→ Додати транспорт в гараж
        │
        └─→ Повернення результату
            │
            └─→ Показати успіх / Перенаправити
```

---

## 🗄️ Модель даних

### Case (Кейс)
```
┌─────────────────────────────┐
│ Case                        │
├─────────────────────────────┤
│ id (PK)                     │
│ name (CharField)            │
│ description (TextField)     │
│ rarity (CharField)          │
│ price (DecimalField)        │
│ image (ImageField)          │
│ is_active (BooleanField)    │
│ created_at (DateTimeField)  │
└─────────────────────────────┘
         ↑
         │ 1:M
         │
┌─────────────────────────────┐
│ CaseReward                  │
├─────────────────────────────┤
│ id (PK)                     │
│ case (FK)                   │
│ vehicle_type (CharField)    │
│ car (FK) ├→ Cars           │
│ atv (FK) ├→ Atvs           │
│ moped (FK) ├→ Moped        │
│ motocycle (FK) ├→ Motocycles│
│ probability (IntegerField)  │
│ created_at (DateTimeField)  │
└─────────────────────────────┘
```

### OpenedCase (Історія)
```
┌──────────────────────────────┐
│ OpenedCase                   │
├──────────────────────────────┤
│ id (PK)                      │
│ case (FK) ───→ Case         │
│ reward (FK) ──→ CaseReward   │
│ opened_at (DateTimeField)    │
└──────────────────────────────┘
```

---

## 🔗 Зв'язки між моделями

```
Case (1)
  │
  └─→ (M) CaseReward
        │
        ├─→ (1) Cars
        ├─→ (1) Atvs
        ├─→ (1) Moped
        └─→ (1) Motocycles

OpenedCase (M)
  ├─→ (1) Case
  └─→ (1) CaseReward
         └─→ (1) Любої Garage через GarageItem
```

---

## 🎯 API Endpoints

| Метод | URL | View | Функція |
|-------|-----|------|---------|
| GET | `/cases/` | case_list | Список кейсів |
| GET | `/cases/<id>/` | case_detail | Деталі кейса |
| POST | `/cases/<id>/open/` | open_case | Відкрити кейс |
| POST | `/cases/<id>/open-animation/` | open_case_animation | Z AJAX |
| GET | `/cases/history/` | cases_history | Історія |

---

## 🎨 Шаблони і статичні файли

### Templates (HTML)
```
cases/templates/cases/
├── case_list.html
│   ├── Bootstrap 5
│   ├── Карточки кейсів
│   └── Статистика
│
├── case_detail.html
│   ├── Інформація про кейс
│   ├── Список нагород
│   ├── Історія розкриттів
│   └── Кнопка "Відкрити"
│
└── history.html
    ├── Таблиця розкриттів
    └── Статистика
```

### Стилі
- Bootstrap 5 CDN
- Custom CSS (inline в шаблонах)
- Адаптивна верстка

---

## 🔐 Безпека

### На сервері
✅ Генерування вероватності на сервері (не можна обманути)
✅验ерка прав доступу (можна додати)
✅ CSRF захист (автоматичний)

### В БД
✅ Всі розкриття записуються
✅ Неможливо редагувати історію
✅ Каскадне видалення при видаленні кейса

---

## 🚀 Інтеграція з іншими компонентами

### З гаражем
- При відкритті кейса транспорт додається в Garage
- Якщо гаража немає - створюється автоматично

### З типами транспорту
- Всі типи (Cars, Atvs, Moped, Motocycles) вже існують
- Система полімерна - працює з будь-яким типом

### З адміном
- Повна інтеграція з Django admin
- Управління кейсами, нагородами, історією

---

## 📈 Масштабованість

### Можливості розширення

```
Поточна архітектура дозволяє:

1. Додавання нових типів транспорту
   - Просто додати нову модель
   - Додати в CaseReward.VEHICLE_TYPES

2. Система платежу
   - Додати Payment модель
   - Інтегрувати Stripe/PayPal

3. Множинні користувачі
   - Додати User FK до OpenedCase
   - Статистика на користувача

4. Торгівля кейсами
   - Додати Price модель
   - Система позицій в інвентарі

5. Батли кейсів
   - Додати Competition модель
   - Система перемог/поразок
```

---

## ✨ Окремі особливості

- **Вероватність** - Гнучка система з будь-якими числами
- **Історія** - Повна статистика всіх розкриттів
- **Адмін** - Зручне управління через Django admin
- **Design** - Красивий UI з Bootstrap 5
- **Мобільна** - Адаптивна верстка для всіх пристроїв

---

## 🔄 Цикл життя даних

```
Створення кейса (адмін)
    ↓
Додавання нагород (адмін)
    ↓
Користувач переглядає список
    ↓
Користувач вибирає кейс
    ↓
Користувач натискає "Відкрити"
    ↓
Система генерує нагороду
    ↓
Запис в OpenedCase (історія)
    ↓
Додавання в GarageItem
    ↓
Показ результату користувачу
    ↓
Транспорт видимий в гаражі
```

---

**Архітектура оптимізована для простоти, гнучкості та масштабованості! 🚀**
