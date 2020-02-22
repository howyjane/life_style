from django.urls import path
from .views import home, aboutus, change_password, reset_password # .views refer to the views.py in the current directory as this file

urlpatterns = [
    path('', home, name='home' ),
    path('aboutus', aboutus, name='aboutus' ),
    path('change_password',change_password , name='change_password' ),
    path('reset_password',reset_password , name='reset_password' ),
  
    
   
   
    
]

