from django.db import models
from accounts.models import User  # Import your custom User model

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes', default=1)  # Foreign key to User
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f'{self.source} - {self.amount}'

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses', default=1)  # Replace 1 with a valid user ID # Foreign key to User
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f'{self.category} - {self.amount}'

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='goals')  # Change related_name
    name = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    target_date = models.DateField()
    category = models.CharField(max_length=255, default='Uncategorized')

    def __str__(self):
        return f'{self.name} - Target: {self.target_amount} - Current: {self.current_amount}'
