from django.shortcuts import render
from django.http import HttpResponse

from cars.models import Cars
from mopeds.models import Moped
from motocycles.models import Motocycles
from atvs.models import Atvs


def home(request):
    # Підрахунок записів для dashboard
    cars_count = Cars.objects.count()
    mopeds_count = Moped.objects.count()
    motocycles_count = Motocycles.objects.count()
    atvs_count = Atvs.objects.count()
    latest_cars = Cars.objects.all().order_by('-id')[:5]

    context = {
        'cars_count': cars_count,
        'mopeds_count': mopeds_count,
        'motocycles_count': motocycles_count,
        'atvs_count': atvs_count,
        'latest_cars': latest_cars,
    }
    return render(request, 'dashboard.html', context)

# Create your views here.


