from django import forms
from .models import Course
from pyuploadcare.dj.forms import ImageField

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'

class CourseSearchForm(forms.Form):
    search_terms = forms.CharField(required=False)




