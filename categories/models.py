from django.conf import settings
from django.db import models

# Global Category (admin-created)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, default='No description available')

    def __str__(self):
        return self.name

# User-Specific Category (user-created)
class UserCategory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.name}"
