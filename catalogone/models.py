from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class CoursePass(models.Model):
    title = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    cost = models.FloatField(blank=False)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return self.title

