from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'target_date', 'description']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'}),
        }
