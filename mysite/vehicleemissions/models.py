from django.db import models

# Create your models here.


class CarClass(models.Model):
    make = models.CharField(max_length=200)
    carModel = models.CharField(max_length=200)
    year = models.IntegerField()
    make2=models.CharField(max_length=200)
    carModel2=models.CharField(max_length=200)
    year2=models.IntegerField()
    def __str__(self):
        return self.make + " " + self.model + " " + str(self.year)
