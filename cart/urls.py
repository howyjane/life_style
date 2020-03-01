from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, add_quantity, minus_quantity


urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<course_id>', add_to_cart, name='add_to_cart'),
    path('add/<CoursePass_id>', add_to_cart, name='add_to_cart'),
    path('remove/<course_id>', remove_from_cart, name='remove_from_cart'),
    path('add_quantity/<course_id>', add_quantity, name='add_quantity'),
    path('minus_quantity/<course_id>', minus_quantity, name='minus_quantity'),
    


    
    
  
]

