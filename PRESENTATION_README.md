# Presentation Context — MyProject

## Purpose & Audience
- **Purpose:** Представити поточний стан проєкту, продемонструвати нову функцію "Створити гараж" і уніфікований інтерфейс для сторінок транспортних засобів.
- **Audience:** менеджмент + технічна команда (можливі замовники). Тон: напівтехнічний, демонстрація з прикладами.

## Key Messages
1. Уніфікація UI: домашні сторінки транспортних засобів приведені до єдиного стилю.
2. Покращені списки/таблиці: оновлений, сучасний вигляд переліків.
3. Нова функціональність: форма створення гаража (`garage_create`) з повною інтеграцією в UI.
4. Наступні кроки: тестування, UI-репліки, додавання кнопки створення в KPI-блок на дашборді.

## Suggested Slide List
- Title slide: назва, ведучі, дата
- Problem / Context: навіщо потрібна зміна UI та функція гаража
- Solution overview: що змінено (UI, списки, CRUD для гаража)
- Demo: коротка жива демонстрація або скріншоти
- Technical snapshot: файли та архітектура
- Metrics / QA: план тестів і очікувані перевірки
- Next steps & timeline
- Q&A / Appendix (технічні деталі)

## Relevant Files (in repo)
- Dashboard & links: [main/templates/dashboard.html](main/templates/dashboard.html)
- Garage create form & view: [garage/forms.py](garage/forms.py), [garage/views.py](garage/views.py), [garage/urls.py](garage/urls.py)
- Garage templates: [garage/templates/create_garage.html](garage/templates/create_garage.html), [garage/templates/garage_list.html](garage/templates/garage_list.html), [garage/templates/garage_detail.html](garage/templates/garage_detail.html)
- Example home/list templates: [cars/templates/cars_home.html](cars/templates/cars_home.html), [cars/templates/cars.html](cars/templates/cars.html)
- Other vehicle templates updated: `atvs`, `mopeds`, `motocycles` templates under their respective templates folders.

## Assets to Gather
- Screenshots of `cars_home`, `garage_list` (empty and with items), `create_garage` form, and `dashboard` quick-actions.
- Any relevant metrics (DB counts, usage stats) and test outputs.
- Code snippets for the demo: short excerpt showing `GarageForm` and `create_garage` view.

## How to run locally (for screenshots / demo)
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt  # if you have one
python manage.py migrate
python manage.py runserver
# Open http://127.0.0.1:8000/ to access dashboard
# Create garage demo: http://127.0.0.1:8000/garage/create/
```

Note: the dev server previously failed with exit code 1 in this workspace; run locally and check server logs if errors appear.

## Roles & Schedule
- Presenter: (assign name)
- Demo lead: (assign name)
- Designer: (assign name)
- Timeline: draft → review → final (suggest 3–5 working days total, plus 1–2 rehearsals)

## Q&A Prep
- Be ready to explain redirect flow after garage creation, where templates live, and how to adjust UI.
- Appendix slides: code snippets, migration notes, list of updated templates.

---
Created automatically to support presentation prep. If хочеш, можу: 1) зібрати скріншоти й список змін по файлах; 2) згенерувати PPTX із базовими слайдами; 3) додати короткі нотатки для кожного слайда.