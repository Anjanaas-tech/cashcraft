from django.db import models
from django.conf import settings

class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Default Title")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    source = models.CharField(max_length=100, default="Unknown")  
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.amount} from {self.source}"
