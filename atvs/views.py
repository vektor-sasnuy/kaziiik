from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Atvs
from .forms import AtvsForm


def atvs_home(request):
    atvs = Atvs.objects.all()
    atvs_count = atvs.count()
    return render(request, 'atvs_home.html', {'atvs': atvs, 'atvs_count': atvs_count})


def atvs_detail(request):
    return HttpResponse(f"Details for atv with ID (stub).")


def atvs_create(request):
    if request.method == 'POST':
        form = AtvsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atv_list')
    else:
        form = AtvsForm()
    return render(request, 'atvs_create.html', {'form': form})


def mopeds_list(request):
    atvs = Atvs.objects.all()
    return render(request, 'atvs.html', {'atvs': atvs})

