from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.template.html')

def aboutus(request):
    return render(request, 'home/aboutus.template.html')