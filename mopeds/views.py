from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Moped
from .forms import MopedForm

# Create your views here.
def mopeds_home(request):
    mopeds = Moped.objects.all()
    mopeds_count = mopeds.count()
    return render(request, 'mopeds_home.html', {'mopeds': mopeds, 'mopeds_count': mopeds_count})

# написати view для повної інформації про мопед (поки що заглушка)       
def moped_detail(request):
    return HttpResponse(f"Details for moped with ID (stub).")
# написати view для створення нового мопеда (поки що заглушка)


def moped_create(request):
    if request.method == 'POST':
        form = MopedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mopeds_list')
    else:
        form = MopedForm()
    return render(request, 'mopeds_create.html', {'form': form})


def mopeds_list(request):
    # Отримуємо всі об'єкти мопедів
    mopeds = Moped.objects.all()
    # Повертаємо список мопедів у контексті
    return render(request, 'index.html', {'mopeds': mopeds})
