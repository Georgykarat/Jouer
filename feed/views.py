from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from home.models import CustomUser
from django.conf import settings
from home.views import is_ajax


class Design:
    """Class for getting design details"""
    def __init__(self):
        self.color1 = settings.COLOR1


class Person:
    """Class for getting user data"""
    def __init__(self, request):
        self.mail = request.user.username
        self.userdata = CustomUser.objects.filter(user=request.user).values().get()
        self.firstname = self.userdata['first_name']
        self.lastname = self.userdata['last_name']
        self.sex = self.userdata['sex']
        self.country = self.userdata['country']
        self.city = self.userdata['city']
        self.phone = self.userdata['phone']
        self.cordinates = self.userdata['cordinates']
        self.access = self.userdata['access']
        self.verified = self.userdata['verified']
        self.image_path = self.userdata['image_path']
        if self.userdata['nickname']:
            self.nickname = self.userdata['nickname']
        else:
            self.nickname = self.mail


# Create your views here.

def feed(request):
    """Provides users the ability to see the feed"""
    if request.user.is_authenticated == True:
        CurrentDesign = Design()
        CurrentUser = Person(request)
        return render(request, 'feed/feed.html', {
            'page': 'workspace',
            'cuser': CurrentUser,
            'design': CurrentDesign,
        })
    else:
        return HttpResponseRedirect('/login/')
    

def usettings(request):
    """View for profile settings page"""
    if request.user.is_authenticated == True:
        CurrentUser = Person(request)
        CurrentDesign = Design()
        return render(request, 'settings/settings.html', {
            'page': 'settings',
            'cuser': CurrentUser,
            'design': CurrentDesign,
        })
    else:
        return HttpResponseRedirect('/login/')


def usettings_changepass(request):
    if request.user.is_authenticated == True:
        if is_ajax(request=request):
            oldpass1 = request.POST['oldpass']
            oldpass2 = request.POST['oldpass2']
            newpass = request.POST['newpass']
        else:
            return JsonResponse({}, status=400)
    else:
        return HttpResponseRedirect('/login/')    

# def logout(request):
#     """Provides users the ability to logout (func)"""
#     return HttpResponseRedirect('/')


class MainLogoutView(LogoutView):
    """Provides users the ability to logout (class)"""
    next_page = '/'