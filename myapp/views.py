from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Welcome to Django")


def info(request):
    return HttpResponse("this is python 3.9")

def input(request):
    return HttpResponse("Enter the number: ")

def watch(request):
    return HttpResponse("<h1>Watch</h1>")

def home(request):
    sitename = "Django"
    moto = "Django is awesome!!!"
    return render(request,'index.html',{'name':sitename,'moto':moto})