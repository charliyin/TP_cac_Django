from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ContactoForms

# Create your views here.

def index(request):
    return render(request,"TPapp/index.html")

def contacto(request):
    data = {
        'form' : ContactoForms()
    }
    if request.method =='POST':
        formulario = ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    

    return render(request,"TPapp/contacto.html", data)

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
