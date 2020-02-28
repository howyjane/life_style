from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm




# Create your views here.


# def signup_view(request):
#     form = SignUpForm(request.POST)
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


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


@login_required
def profile(request):
    return render(request, 'profile.html',{
        'current_user':request.user
    })


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
    return render(request, 'signup.html', {'form': form})
    

@login_required
def update_profile(request):
    if request.method == 'POST':
        update_profile_form = ProfileForm(request.POST, instance=request.request.user)
        if update_profile.is_valid():
            update_profile.save()
            
            return redirect('settings:profile')
    
    else:
            update_profile_form = ProfileForm(instance=request.request.user)
    return render(request, 'profile.html', {
        'ProfileForm': update_profile_form
    })

