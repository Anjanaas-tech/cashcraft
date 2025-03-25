from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ["name", "target_amount", "current_balance", "allocated_amount"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "border p-2 w-full rounded"}),
            "target_amount": forms.NumberInput(attrs={"class": "border p-2 w-full rounded"}),
            "current_balance": forms.NumberInput(attrs={"class": "border p-2 w-full rounded"}),
            "allocated_amount": forms.NumberInput(attrs={"class": "border p-2 w-full rounded"}),
        }
