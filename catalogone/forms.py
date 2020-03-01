from django import forms
from .models import CoursePass
from pyuploadcare.dj.forms import ImageField

class CoursePassForm(forms.ModelForm):
    class Meta:
        model=CoursePass
        fields='__all__'