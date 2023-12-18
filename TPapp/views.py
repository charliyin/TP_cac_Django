from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request,"TPapp/index.html")


def contacto(request):
    return render(request,"TPapp/contacto.html")

@login_required
def remuneraciones(request):
    return render(request,"TPapp/remuneraciones.html")

def login(request):
    return render(request,"TPapp/login.html")

def personal(request):
    return render(request,"TPapp/personal.html")

def exit(request):
    logout(request)
    return redirect('index')

def trabajadores(request):
    return render(request,"")