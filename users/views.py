from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm

# Create your views here.

# Index.html
@login_required
def home(request):
    return render(request, 'home.html')

# User Registration 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


#import this at the top of the page

# user profile authentication required
@login_required
def profile(request):
    return render(request, 'profile.html',{
        'current_user':request.user
    })

# admin registration authentication required 
@login_required
def admin_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'admin_signup.html', {'form': form})
    
# update user profile authentication required 
@login_required
def update_profile(request):
    print("update")
    if request.method == 'POST':
        update_profile_form = ProfileForm(request.POST, instance=request.user)
        if update_profile_form.is_valid():
            update_profile_form.save()
            
             # always make sure to return the redirect
            return redirect(reverse(update_profile))
    
    else:
            update_profile_form = ProfileForm(instance=request.user)
    return render(request, 'update_profile.html', {
        'ProfileForm': update_profile_form
    })

