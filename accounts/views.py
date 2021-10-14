from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as dj_login

# Create your views here.

# def getstarted_individual(request):
#     return render(request, 'accounts/individual.html')

def getstarted_business(request):
    if request.method == 'POST':
        fullname = request.POST['businessname']
        username = request.POST['username']
        password = request.POST['password']
        password = request.POST['passwordagain']
        phonenumber = request.POST['phonenumber']
        
        print(request.POST)
        myuser = User.objects.create_user(fullname=fullname, username=username, password=password, phonenumber=phonenumber, buisness='business')
        myuser.save()
    return render(request, 'accounts/buisness.html')


def login(request):
    return render(request, 'accounts/login.html')


def CreateUser(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        password = request.POST['passwordagain']
        phonenumber = request.POST['phonenumber']
        
        print(request.POST)
        myuser = User.objects.create_user(fullname=fullname, username=username, password=password, phonenumber=phonenumber, individual='individual')
        myuser.save()

    return render(request, 'accounts/individual.html')


def CreateLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                dj_login(request,user)
                return redirect('landingpage')

            else:
                return redirect(login)

        else:
            return redirect('landingpage')

    return render(request, "accounts/login.html")
        
