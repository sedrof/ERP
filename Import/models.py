from django.db import models
from Category.models import Category

class Import(models.Model):
    Date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.Date} - {self.quantity}"