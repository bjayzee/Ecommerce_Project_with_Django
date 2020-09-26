from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Setting up home page")

# Create your views here.
