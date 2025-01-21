from django.conf import settings
from django.db import models
from accounts.models import User


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"
