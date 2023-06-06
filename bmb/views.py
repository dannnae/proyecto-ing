from django.shortcuts import render
from .models import *

def index(request):
    return render(request, "index.html")

def index2(request):
    return render(request, "index2.html")
