from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Import your custom User model

# Customize the User Admin Interface
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'is_active', 'is_staff')  # Fields displayed in admin
    search_fields = ('email', 'username')  # Enable search functionality
    ordering = ('id',)  # Order users by ID
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

# Register the model
admin.site.register(User, CustomUserAdmin)
