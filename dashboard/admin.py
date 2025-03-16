from django.contrib import admin
from .models import Income, Expense, Goal

# ------------------- Income -------------------
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'source', 'amount', 'date')
    search_fields = ('user__username', 'source')
    list_filter = ('source', 'date')

# ------------------- Expense -------------------
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'date')
    search_fields = ('user__username', 'category')
    list_filter = ('category', 'date')

# ------------------- Goal -------------------
class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'target_amount', 'current_amount', 'target_date', 'category')
    search_fields = ('user__username', 'name', 'category')
    list_filter = ('category', 'target_date')

# ------------------- Register -------------------
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Goal, GoalAdmin)
