from django import forms
from .models import GarageItem, Garage
from cars.models import Cars
from atvs.models import Atvs
from mopeds.models import Moped
from motocycles.models import Motocycles


class GarageItemForm(forms.Form):
    VEHICLE_TYPES = (
        ('car', 'Car'),
        ('atv', 'ATV'),
        ('moped', 'Moped'),
        ('motocycle', 'Motocycle'),
    )
    
    vehicle_type = forms.ChoiceField(
        choices=VEHICLE_TYPES, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Vehicle Type'
    )
    
    car = forms.ModelChoiceField(
        queryset=Cars.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Select Car'
    )
    
    atv = forms.ModelChoiceField(
        queryset=Atvs.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Select ATV'
    )
    
    moped = forms.ModelChoiceField(
        queryset=Moped.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Select Moped'
    )
    
    motocycle = forms.ModelChoiceField(
        queryset=Motocycles.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Select Motocycle'
    )


class GarageForm(forms.ModelForm):
    class Meta:
        model = Garage
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Garage name'})
        }
        labels = {
            'name': 'Garage name'
        }
