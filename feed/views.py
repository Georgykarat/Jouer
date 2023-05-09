from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def feed(request):
    if request.user.is_authenticated == True:
        return render(request, 'feed/feed.html')
    else:
        return HttpResponseRedirect('/login')