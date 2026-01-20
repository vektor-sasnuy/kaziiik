from django import forms
from .models import Case


class CaseOpenForm(forms.Form):
    """Форма для відкриття кейса"""
    case = forms.ModelChoiceField(
        queryset=Case.objects.filter(is_active=True),
        widget=forms.RadioSelect,
        empty_label=None,
        label='Виберіть кейс'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['case'].queryset = Case.objects.filter(is_active=True)
