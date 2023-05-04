from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse


# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'home/home.html', {
    })


