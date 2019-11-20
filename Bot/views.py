from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Data
# Create your views here.
import pywinauto

def voice():
    pywinauto.keyboard.send_keys("{VK_LWIN down}r{VK_LWIN up}")

def on_mic(request):
    voice()
    return redirect('/')

def home(request):
    obj = Data()
    return render(request,'index.html',{'obj':obj})

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == "POST":

        uname = request.POST['uname']
        psw = request.POST['psw']

        user = auth.authenticate(username=uname,password=psw)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credintials')
            return redirect('/')


        return redirect('/')
    else:
        return render(request,'login.html')

def register(request):

    if request.method == "POST":
        uname = request.POST['uname']
        gmail = request.POST['gmail']
        pwd = request.POST['psw']
        cpwd = request.POST['psw-repeat']

        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=gmail).exists():
                    messages.info(request,'gmail already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=uname,password=pwd,email=gmail)
                    user.save()
                    messages.info(request,'Registeration is successfull')
                    return redirect('/')


        else:
            messages.info(request,'password are not matched')
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'register.html')