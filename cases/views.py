from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Case, OpenedCase, CaseReward
from .forms import CaseOpenForm
from garage.models import Garage, GarageItem


def case_list(request):
    """Список всех доступных кейсов"""
    cases = Case.objects.filter(is_active=True)
    
    # Получить статистику
    stats = {}
    for case in cases:
        stats[case.id] = {
            'opened_count': case.opened_cases.count(),
            'rewards_count': case.rewards.count(),
        }
    
    return render(request, 'cases/case_list.html', {
        'cases': cases,
        'stats': stats,
    })


def case_detail(request, pk):
    """Деталі кейса та його нагород"""
    case = get_object_or_404(Case, pk=pk, is_active=True)
    rewards = case.rewards.all().select_related('car', 'atv', 'moped', 'motocycle')
    history = case.opened_cases.all()[:10]
    
    return render(request, 'cases/case_detail.html', {
        'case': case,
        'rewards': rewards,
        'history': history,
    })


def open_case(request, pk):
    """Відкрити кейс та отримати нагороду"""
    case = get_object_or_404(Case, pk=pk, is_active=True)
    
    if request.method == 'POST':
        # Отримати випадкову нагороду
        reward = OpenedCase.get_random_reward(case)
        
        if reward:
            # Створити запис про відкритий кейс
            opened = OpenedCase.objects.create(case=case, reward=reward)
            
            # Додати в гараж, якщо є гараж
            garages = Garage.objects.all()
            if garages.exists():
                garage = garages.first()
            else:
                garage = Garage.objects.create()
            GarageItem.objects.create(
                garage=garage,
                vehicle_type=reward.vehicle_type,
                **{reward.vehicle_type: reward.get_vehicle()}
            )
            
            messages.success(request, f"Кейс відкрито! Ви отримали: {reward.get_vehicle().name}")
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                vehicle = reward.get_vehicle()
                return JsonResponse({
                    'success': True,
                    'vehicle_name': vehicle.name,
                    'vehicle_type': reward.vehicle_type,
                    'rarity': case.get_rarity_display(),
                })
            
            return redirect('cases:case_detail', pk=case.pk)
        else:
            messages.error(request, "У цьому кейсі немає нагород!")
            return redirect('cases:case_detail', pk=case.pk)
    
    return redirect('cases:case_detail', pk=case.pk)


def open_case_animation(request, pk):
    """Сторінка з анімацією відкриття кейса"""
    case = get_object_or_404(Case, pk=pk, is_active=True)
    rewards = case.rewards.all().select_related('car', 'atv', 'moped', 'motocycle')
    
    if request.method == 'POST':
        reward = OpenedCase.get_random_reward(case)
        
        if reward:
            opened = OpenedCase.objects.create(case=case, reward=reward)
            
            # Додати в гараж
            garages = Garage.objects.all()
            if garages.exists():
                garage = garages.first()
            else:
                garage = Garage.objects.create()
            GarageItem.objects.create(
                garage=garage,
                vehicle_type=reward.vehicle_type,
                **{reward.vehicle_type: reward.get_vehicle()}
            )
            
            vehicle = reward.get_vehicle()
            return JsonResponse({
                'success': True,
                'reward_id': reward.id,
                'vehicle_name': vehicle.name,
                'vehicle_type': reward.vehicle_type,
                'vehicle_type_label': reward.get_vehicle_type_display(),
                'rarity': case.get_rarity_display(),
                'case_name': case.name,
            })
        else:
            return JsonResponse({'success': False, 'error': 'No rewards available'})
    
    return render(request, 'cases/case_open_animation.html', {
        'case': case,
        'rewards': rewards,
    })


def cases_history(request):
    """Історія відкритих кейсів"""
    history = OpenedCase.objects.all().select_related('case', 'reward')
    
    # Статистика
    total_opened = history.count()
    unique_cases = history.values('case').distinct().count()
    
    return render(request, 'cases/history.html', {
        'history': history,
        'total_opened': total_opened,
        'unique_cases': unique_cases,
    })
