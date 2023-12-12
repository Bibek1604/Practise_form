from django.shortcuts import render
from django.http import HttpResponse
from  practiseonly.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages,redirects
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render (request , 'index.html')

def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

# In your app's views.py file

def contact(request):
    print(request.POST)
    if  request.method == 'POST':
        # print("hello world")
        name = request.POST['name']
        email = request.POST['email']
        phn = request.POST['phn']
        message = request.POST['message']
        # print(name , email ,phn , message)
        contact= Contact(name=name, email=email ,phn=phn ,message=message)
        contact.save()
        print("the data had been Send .")
        
    return render(request,'contact.html')

def login(request):
    return render(request, 'login.html')
        
        
