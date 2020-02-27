from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Course(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    
    )
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    
    TIME_CHOICES = (
        ('8.00am', '8.00am'),
        ('9.00am', '9.00am'),
        ('10.00am', '10.00am'),
        ('11.00am', '11.00am'),
        ('12.00pm', '12.00pm'),
        ('1.00pm', '1.00pm'),
        ('2.00pm', '2.00pm'),
        ('3.00pm', '3.00pm'),
        ('4.00pm', '4.00pm'),
        ('5.00pm', '5.00pm'),
        ('6.00pm', '6.00pm'),
        ('7.00pm', '7.00pm'),
  
        

    )
    start_time = models.CharField(max_length=10, choices=TIME_CHOICES)
    
    # start_time = models.IntegerField(blank=False)
    
    # TIME_CHOICES = (
    #     ('am', 'am'),
    #     ('pm', 'pm'),

    # )
    # name= models.CharField(max_length=60)
    # time = models.CharField(max_length=1, choices=TIME_CHOICES)
    
    title = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    number_of_minutes = models.IntegerField(blank=False)
    instructor = models.ForeignKey('Instructor', blank=True, null=True, on_delete=models.SET_NULL)
    image = ImageField(null=True)
    cost = models.FloatField(blank=False)
    quantity = models.IntegerField(blank=False)
    
    
    def __str__(self):
        return self.title
    
class Instructor(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

