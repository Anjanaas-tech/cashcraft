from django.db import models
from django.conf import settings

class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default='General')  # <== THIS MUST EXIST
    item = models.CharField(max_length=200, blank=True, null=True)  # <== ITEM FIELD
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
