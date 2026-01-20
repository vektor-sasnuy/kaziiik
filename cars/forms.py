from django import forms
from .models import Cars


class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['name', 'body', 'motor', 'gear_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва машини'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тип кузова'}),
            'motor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Об\'єм двигуна', 'step': '0.1'}),
            'gear_type': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'name': 'Назва машини',
            'body': 'Тип кузова',
            'motor': 'Об\'єм двигуна',
            'gear_type': 'Автоматична коробка передач',
        }
