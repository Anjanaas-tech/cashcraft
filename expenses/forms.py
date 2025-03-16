from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'date', 'description']  # Added date & description fields
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Date picker
            'description': forms.Textarea(attrs={'rows': 3}),
        }
