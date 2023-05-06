from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse


# Create your views here.

def home(request, *args, **kwargs):
    """Function to render home page
    Args:
        request ([request]): [just request via url]
    Returns:
        [render func]: [render home page]
    """
    return render(request, 'home/home.html', {
    })


def signup(request, *args, **kwargs):
    """Function to render signup page
    Args:
        request ([request]): [just request via url]
    Returns:
        [render func]: [render signup page]
    """
    return render(request, 'home/signup.html', {
    })


def login(request, *args, **kwargs):
    """Function to render login page
    Args:
        request ([request]): [just request via url]
    Returns:
        [render func]: [render login page]
    """
    return render(request, 'home/login.html', {
    })