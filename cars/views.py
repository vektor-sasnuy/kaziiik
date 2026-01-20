from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cars
from .forms import CarsForm


def cars_home(request):
    cars = Cars.objects.all()
    cars_count = cars.count()
    return render(request, 'cars_home.html', {'cars': cars, 'cars_count': cars_count})


def cars_detail(request):
    return render(f"Details for car with ID (stub).")


def cars_create(request):
    if request.method == 'POST':
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarsForm()
    return render(request, 'cars_create.html', {'form': form})


def cars_list(request):
    # Отримуємо всі об'єкти машин
    cars = Cars.objects.all()
    # Повертаємо список машин у контексті
    return render(request, 'cars.html', {"cars": cars})


# створення нової машини