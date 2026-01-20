from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Garage, GarageItem
from .forms import GarageItemForm, GarageForm
from cars.models import Cars
from atvs.models import Atvs
from mopeds.models import Moped
from motocycles.models import Motocycles


def garage_list(request):
    garages = Garage.objects.all()
    if not garages.exists():
        Garage.objects.create(name="My Garage")
        garages = Garage.objects.all()
    return render(request, 'garage_list.html', {'garages': garages})


def garage_detail(request, pk):
    garage = get_object_or_404(Garage, pk=pk)
    items = garage.items.all()
    cars = Cars.objects.all()
    atvs = Atvs.objects.all()
    mopeds = Moped.objects.all()
    motocycles = Motocycles.objects.all()
    
    return render(request, 'garage_detail.html', {
        'garage': garage,
        'items': items,
        'cars': cars,
        'atvs': atvs,
        'mopeds': mopeds,
        'motocycles': motocycles,
    })


def add_to_garage(request, garage_pk):
    garage = get_object_or_404(Garage, pk=garage_pk)
    
    if request.method == 'POST':
        form = GarageItemForm(request.POST)
        if form.is_valid():
            vehicle_type = form.cleaned_data['vehicle_type']
            
            garage_item = GarageItem(garage=garage, vehicle_type=vehicle_type)
            
            if vehicle_type == 'car':
                garage_item.car = form.cleaned_data['car']
            elif vehicle_type == 'atv':
                garage_item.atv = form.cleaned_data['atv']
            elif vehicle_type == 'moped':
                garage_item.moped = form.cleaned_data['moped']
            elif vehicle_type == 'motocycle':
                garage_item.motocycle = form.cleaned_data['motocycle']
            
            garage_item.save()
            messages.success(request, f"Vehicle added to garage successfully!")
            return redirect('garage_detail', pk=garage_pk)
    else:
        form = GarageItemForm()
    
    return render(request, 'add_to_garage.html', {'form': form, 'garage': garage})


def create_garage(request):
    if request.method == 'POST':
        form = GarageForm(request.POST)
        if form.is_valid():
            garage = form.save()
            messages.success(request, "Garage created successfully!")
            return redirect('garage_detail', pk=garage.pk)
    else:
        form = GarageForm()
    return render(request, 'create_garage.html', {'form': form})


def remove_from_garage(request, garage_pk, item_pk):
    garage = get_object_or_404(Garage, pk=garage_pk)
    item = get_object_or_404(GarageItem, pk=item_pk, garage=garage)
    item.delete()
    messages.success(request, "Vehicle removed from garage!")
    return redirect('garage_detail', pk=garage_pk)
