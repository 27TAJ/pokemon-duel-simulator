from django.shortcuts import render
from rest_framework import generics


# Create your views here.

def index(request):
    return render(request, 'index.html')

#homepage view
def home(request):
    return render(request, 'home.html')
#about page view
def about(request):
    return render(request, 'about.html')
#support page view
def support(request):
    return render(request, 'support.html')