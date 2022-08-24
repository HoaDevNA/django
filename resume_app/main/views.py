from django.shortcuts import render
from main.models import Course
# Create your views here.
def index(request):
    object_list = Course.objects.all()
    return render(request, 'home.html', {
        'object_list': object_list,
        'nav': 'home'
    })

def login(request):
    return render(request, 'login.html',{
        'nav': 'login'
    })
def register(request):
    return render(request, 'register.html')