from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Cart(models.Model):
    title = models.CharField(blank=False, max_length=255)
    # desc = models.TextField(blank=False)
    # number_of_minutes = models.IntegerField(blank=False)
    # instructor = models.ForeignKey('Instructor', blank=True, null=True, on_delete=models.SET_NULL)
    # image = ImageField(null=True)
    cost = models.FloatField(blank=False)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    quantity = models.FloatField(default=1)

    def __str__(self):
        return self.title
    
class Instructor(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name




