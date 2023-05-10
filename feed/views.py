from django.http import HttpResponseRedirect
from django.contrib.auth.views import LogoutView
from django.shortcuts import render

# Create your views here.

def feed(request):
    if request.user.is_authenticated == True:
        return render(request, 'feed/feed.html')
    else:
        return HttpResponseRedirect('/login/')
    

# def logout(request):
#     """Provides users the ability to logout (func)"""
#     return HttpResponseRedirect('/')


class MainLogoutView(LogoutView):
    """Provides users the ability to logout (class)"""
    next_page = '/'