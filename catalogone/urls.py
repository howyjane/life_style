from django.urls import path
from .views import show_pass, create_pass  # .views refer to the views.py in the current directory as this file
from django.views.decorators.csrf import csrf_exempt 


urlpatterns = [
   
    path('', show_pass, name='show_pass'),
    path('create', create_pass, name='create_pass'),


]