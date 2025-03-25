from django.db import models

class Goal(models.Model):
    name = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    @property
    def remaining_amount(self):
        return self.target_amount - (self.current_balance + self.allocated_amount)

    def __str__(self):
        return self.name
