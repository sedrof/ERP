from django.db import models
from Category.models import Category

class Export(models.Model):
    Date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    invoice_number = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.Date} - {self.invoice_number} - {self.quantity}"