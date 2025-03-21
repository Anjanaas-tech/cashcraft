from django.contrib import admin
from .models import Goal

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'target_amount', 'target_date', 'calculate_progress_display')
    list_filter = ('target_date',)
    search_fields = ('name',)
    ordering = ('target_date',)
    list_per_page = 20

    # Custom method to display progress nicely
    def calculate_progress_display(self, obj):
        return f"{obj.calculate_progress:.1f}%"
    calculate_progress_display.short_description = 'Progress'

    # Optional: Add editable fields in list view
    list_editable = ('target_amount', 'target_date',)

    # Optional: Add date hierarchy for better navigation
    date_hierarchy = 'target_date'

    # Optional: Customize fieldsets in edit view
    fieldsets = (
        ('Goal Information', {
            'fields': ('name', 'target_amount', 'target_date')
        }),
    )
