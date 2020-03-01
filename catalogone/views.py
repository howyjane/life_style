from django.shortcuts import render,  redirect, reverse, get_object_or_404
from .models import CoursePass
from .forms import CoursePassForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def show_pass(request):
    form = CoursePassForm()
    all_coursepass = CoursePass.objects.all()
    return render(request, 'catalogone/course_pass2.template.html', {
        'all_coursepass':all_coursepass,
        'form':form
    })
    
def create_pass(request):
    
        if request.method == 'POST':
            create_course_form = CoursePassForm(request.POST)
            if create_course_form.is_valid():
                newly_created_course = create_course_form.save() 
                messages.success(request, "CoursePass " + newly_created_course.title + " has been created!")
            return redirect(reverse(show_pass))
        else:
            create_course_form = CoursePassForm()
  
        return render(request, 'catalogone/create_pass.template.html', {
        'form':create_course_form

    })
    


