from django.shortcuts import render, redirect
from .models import Category, UserCategory
from .forms import UserCategoryForm  # You'll create this form in the next step

def category_list(request):
    global_categories = Category.objects.all()  # Global categories
    user_categories = UserCategory.objects.filter(user=request.user)  # User-specific categories
    return render(request, 'categories/category_list.html', {
        'global_categories': global_categories,
        'user_categories': user_categories
    })
