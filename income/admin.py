# income/admin.py

from django.contrib import admin
from .models import Income  # Import your model

# Optional: Customize display
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'source', 'date')  # Add fields you want to display
    search_fields = ('user__username', 'source')  # For search bar in admin
    list_filter = ('source', 'date')  # Filters on the right side

admin.site.register(Income, IncomeAdmin)
