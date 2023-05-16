from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from home.models import CustomUser
from django.conf import settings
from home.views import is_ajax
from django.contrib.auth import authenticate, update_session_auth_hash


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
            newpass = request.POST['newpass']
            newpass2 = request.POST['newpass2']
            if oldpass1 != newpass and oldpass1 and newpass and newpass == newpass2:
                user = authenticate(request=request, username=request.user.username, password=oldpass1)
                if user is not None:
                    user.set_password(newpass)
                    user.save()
                    update_session_auth_hash(request, user)
                    return JsonResponse({}, status=200)
                else:
                    return JsonResponse({}, status=400)
            else:
                return JsonResponse({}, status=400)
        else:
            return JsonResponse({}, status=400)
    else:
        return HttpResponseRedirect('/login/')    


def upload_photo(request):
    """Upload photo to profile"""
    if request.method == 'POST':
        # Process the uploaded photo here
        # Save the cropped photo as the profile picture
        if request.user.is_authenticated == True:
            CurrentUser = Person(request)
            CurrentDesign = Design()
            return render(request, 'settings/settings.html', {
                'page': 'settings',
                'cuser': CurrentUser,
                'design': CurrentDesign,
            })
        else:
            return JsonResponse({}, status=400)
    return JsonResponse({}, status=400)


# def logout(request):
#     """Provides users the ability to logout (func)"""
#     return HttpResponseRedirect('/')


class MainLogoutView(LogoutView):
    """Provides users the ability to logout (class)"""
    next_page = '/'