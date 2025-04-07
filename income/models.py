from django.db import models
from accounts.models import User

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=100, default='Uncategorized')
    source = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
       return f"{self.source} - {self.amount}"
