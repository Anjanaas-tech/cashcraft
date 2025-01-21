from django import forms
from .models import UserCategory

class UserCategoryForm(forms.ModelForm):
    class Meta:
        model = UserCategory
        fields = ['name', 'description']
