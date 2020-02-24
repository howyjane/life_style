from django.urls import path
from .views import show_courses, create_course, update_course, confirm_delete_course, actually_delete_course, course_admin, course_search # .views refer to the views.py in the current directory as this file
from django.views.decorators.csrf import csrf_exempt 


urlpatterns = [
    path('', show_courses, name='show_courses'),
    path('create', create_course, name='create_course'),
    path('update/<course_id>', update_course, name='update_course'),
    path('confirm_delete/<course_id>', confirm_delete_course),
    path('actually_delete/<course_id>', actually_delete_course, name='delete_course'),
    path('course_admin', course_admin, name='course_admin'),
    path('course_search', course_search, name='course_search'),
   
]
   





