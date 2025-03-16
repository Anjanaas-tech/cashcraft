from django.conf import settings
from django.db import models
from django.utils import timezone  # Import timezone
from accounts.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Shopping', 'Shopping'),
        ('Rent', 'Rent'),
        ('Other', 'Other'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField(default=timezone.now)  # Default today's date
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - ₹{self.amount} on {self.date}"
