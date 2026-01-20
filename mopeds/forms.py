from django import forms
from .models import Moped


class MopedForm(forms.ModelForm):
    class Meta:
        model = Moped
        fields = ['name', 'body', 'motor', 'starter']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва мопеда'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тип кузова'}),
            'motor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Об\'єм двигуна', 'step': '0.1'}),
            'starter': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'name': 'Назва мопеда',
            'body': 'Тип кузова',
            'motor': 'Об\'єм двигуна',
            'starter': 'Електростартер',
        }
