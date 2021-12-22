from django.shortcuts import render, redirect
from home.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from home.views import *
from .forms import CreateUserForm
from django.contrib.auth.models import User, auth

# Create your views here.
def loginPage(request):
    genres = Category.objects.all()
    myFilter=search(request)
    amt = Cart.objects.count()
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    context={'genres':genres,'amt':amt,'myFilter':myFilter}
    return render(request, 'login.html',context)

def registerPage(request):
    genres = Category.objects.all()
    myFilter=search(request)
    amt = Cart.objects.count()
    form = CreateUserForm()
    if request.method =="POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                auth.login(request, user)
                return redirect('home')     
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
    context={'genres':genres,'myFilter':myFilter,'amt':amt,'form':form}
    return render(request, 'register.html', context)

def forgetpassPage(request):
    return render(request, 'forgetpass.html')
    
def logoutPage(request):
    auth.logout(request)
    return redirect('home')
