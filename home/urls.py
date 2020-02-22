
from django.urls import path
from .views import home, aboutus  # .views refer to the views.py in the current directory as this file

urlpatterns = [
    path('', home, name='home' ),
    path('aboutus', aboutus, name='aboutus' ),
   
    
]

