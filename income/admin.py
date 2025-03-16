from django.contrib import admin
from .models import Income

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'item', 'amount')  # ✅
    list_filter = ('category',)


admin.site.register(Income, IncomeAdmin)
