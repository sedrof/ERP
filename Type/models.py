from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.quantity}"