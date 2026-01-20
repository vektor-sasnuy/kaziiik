from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Motocycles
from .forms import MotocyclesForm

# Create your views here.
def motocycles_home(request):
    motocycles = Motocycles.objects.all()
    motocycles_count = motocycles.count()
    return render(request, 'motocycles_home.html', {'motocycles': motocycles, 'motocycles_count': motocycles_count})

# написати view для повної інформації про мопед (поки що заглушка)       
def motocycles_detail(request):
    return HttpResponse(f"Details for motocycle with ID (stub).")
# написати view для створення нового мопеда (поки що заглушка)                            
def motocycles_create(request):
    if request.method == 'POST':
        form = MotocyclesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('motocycles_list')
    else:
        form = MotocyclesForm()
    return render(request, 'motocycles_create.html', {'form': form})

def motocycles_list(request):
    # Отримуємо всі об'єкти мотоциклів
    motocycles = Motocycles.objects.all()
    # Повертаємо список мотоциклів у контексті
    return render(request, 'motolist.html', {'motocycles': motocycles})


