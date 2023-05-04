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


