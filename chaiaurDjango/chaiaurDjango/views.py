from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    # return HttpResponse("Hello World ! You are at chai aur home page...")
    return render(req, 'website/index.html')

def about(req):
    return HttpResponse("Hello World ! You are at chai aur about page...")

def contact(req):
    return HttpResponse("Hello World ! You are at chai aur contact page...")
