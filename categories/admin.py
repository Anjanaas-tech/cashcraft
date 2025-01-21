from django.contrib import admin
from .models import Category, UserCategory

# Register global categories in the admin panel
admin.site.register(Category)

# Register user-specific categories in the admin panel
admin.site.register(UserCategory)
