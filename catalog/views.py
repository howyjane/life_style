from django.shortcuts import render,  redirect, reverse, get_object_or_404

from .models import Course, Instructor
from .forms import CourseForm, CourseSearchForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_courses(request):
    form = CourseSearchForm()
    all_courses = Course.objects.all()
    return render(request, 'catalog/courses.template.html', {
        'all_courses':all_courses,
        'search_form':form
    })


def create_course(request):
    
        if request.method == 'POST':
            create_course_form = CourseForm(request.POST)
            if create_course_form.is_valid():
                newly_created_course = create_course_form.save() 
                messages.success(request, "Course " + newly_created_course.title + " has been created!")
            return redirect(reverse(show_courses))
        else:
            create_course_form = CourseForm()
  
        return render(request, 'catalog/create_course.template.html', {
        'form':create_course_form

    })

def update_course(request, course_id):
    course_being_updated = get_object_or_404(Course, pk=course_id)
    
    if request.method == "POST":
        # for update
        update_course_form = CourseForm(request.POST, instance=course_being_updated)
        if update_course_form.is_valid():
            update_course_form.save()
         
            # always make sure to return the redirect
            return redirect(reverse(show_courses))
    else:
        update_course_form = CourseForm(instance=course_being_updated)
    
    return render(request, 'catalog/update_course.template.html',{
        'form':update_course_form
    })


def confirm_delete_course(request, course_id):
    course_being_deleted = get_object_or_404(Course, pk=course_id)
    return render(request, 'catalog/confirm_delete_course.template.html', {
        'course':course_being_deleted
    })


def actually_delete_course(request, course_id):
    course_being_deleted = get_object_or_404(Course, pk=course_id)
    course_being_deleted.delete()
    return redirect(reverse('show_courses'))


def course_admin(request):
    form = CourseSearchForm()
    all_courses = Course.objects.all()
    return render(request, 'catalog/course_admin.template.html', {
        'all_courses':all_courses,
        'search_form':form
    })

def course_search(request):
    no_results = False
    form = CourseSearchForm()
    all_courses = Course.objects.all()
    all_instructors = Instructor.objects.all()
    
    # print(request.GET.get('class'))
    selected_courses = Course.objects.all().filter(title=request.GET.get('class')).filter(instructor__first_name=request.GET.get('instructor')).filter(day=request.GET.get('days'))
    if selected_courses.exists():
        pass
    else:
        no_results = True
        
    return render(request, 'catalog/course_search.template.html', {
        'all_courses':all_courses,
        'all_instructors':all_instructors,
        'selected_courses':selected_courses,
        'no_results':no_results,
        
        'search_form':form
    })