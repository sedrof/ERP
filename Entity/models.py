from django.db import models

# Create your models here.
class Entity(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"