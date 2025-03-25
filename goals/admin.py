from django.contrib import admin
from .models import Goal

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("name", "target_amount", "current_balance", "allocated_amount", "remaining_amount")
    search_fields = ("name",)
    list_filter = ("target_amount",)
    readonly_fields = ("remaining_amount",)

    def remaining_amount(self, obj):
        return obj.remaining_amount
    remaining_amount.short_description = "Remaining Amount"
