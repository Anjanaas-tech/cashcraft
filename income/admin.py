from django.contrib import admin
from .models import Income

class IncomeAdmin(admin.ModelAdmin):
    list_display = ['amount', 'date', 'source']
    list_filter = ['date']
    search_fields = ['source', 'amount']

admin.site.register(Income, IncomeAdmin)