from django.db import models
from Adminstrations.models import Adminstrations
from Stages.models import Stages

# Create your models here.


class Schools(models.Model):
    name = models.CharField(max_length=100)
    adminstration =  models.ForeignKey(Adminstrations, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    stage =  models.ManyToManyField(Stages)

    def __str__(self):
        return f" {self.adminstration} - {self.name}"