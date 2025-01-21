from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Sum
from expenses.models import Expense
from income.models import Income

class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Untitled Goal')
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_date = models.DateField()
    progress = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)



def calculate_progress(self):
    total_saved = Income.objects.filter(user=self.user).aggregate(Sum('amount'))['amount__sum'] or 0
    total_spent = Expense.objects.filter(user=self.user).aggregate(Sum('amount'))['amount__sum'] or 0
    net_savings = total_saved - total_spent
    self.progress = min(net_savings, self.target_amount)
    return (self.progress / self.target_amount) * 100

def __str__(self):
        return self.name
