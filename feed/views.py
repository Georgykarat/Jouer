from django.http import HttpResponseRedirect
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from home.models import CustomUser



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
        CurrentUser = Person(request)
        return render(request, 'feed/feed.html', {
            'nickname': CurrentUser.nickname,
        })
    else:
        return HttpResponseRedirect('/login/')
    

# def logout(request):
#     """Provides users the ability to logout (func)"""
#     return HttpResponseRedirect('/')


class MainLogoutView(LogoutView):
    """Provides users the ability to logout (class)"""
    next_page = '/'