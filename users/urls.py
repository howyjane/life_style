from django.urls import path
from .views import signup, profile, admin_signup
urlpatterns = [
    path('signup', signup, name='signup'),
    path('profile', profile, name='profile'),
    path('admin_signup', admin_signup, name='admin_signup'),
   

    
    
    
]


