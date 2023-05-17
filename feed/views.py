from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from home.models import CustomUser
from django.conf import settings
from home.views import is_ajax
from django.contrib.auth import authenticate, update_session_auth_hash
import os
from PIL import Image


class Design:
    """Class for getting design details"""
    def __init__(self):
        self.color1 = settings.COLOR1


class Person:
    """Class for getting user data"""
    def __init__(self, request):
        self.userid = request.user.id
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
            photo = request.FILES['photo']

            # Create the 'temp' directory if it doesn't exist
            if not os.path.exists('temp'):
                os.makedirs('temp')
            # Get extension, to assign proper name later
            allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
            file_extension = photo.name.split('.')[-1].lower()
            if file_extension in allowed_extensions:
                # Check file size
                if photo.size <= 20 * 1024 * 1024:
                    # Save the uploaded photo temporarily
                    photo_path = 'temp/' + str(CurrentUser.userid) + '.' + file_extension
                    with open(photo_path, 'wb') as f:
                        for chunk in photo.chunks():
                            f.write(chunk)

                    # Get the cropping coordinates
                    crop_x = request.POST.get('crop_x')
                    crop_y = request.POST.get('crop_y')
                    crop_width = request.POST.get('crop_width')
                    crop_height = request.POST.get('crop_height')

                    print('crop_x:', crop_x)
                    print('crop_y:', crop_y)
                    print('crop_width:', crop_width)
                    print('crop_height:', crop_height)

                    # Perform error checking for the cropping coordinates
                    if crop_x is None or crop_y is None or crop_width is None or crop_height is None:
                        return render(request, 'upload.html', {'error': 'Invalid cropping coordinates'})
                    try:
                        crop_x = float(crop_x)
                        crop_y = float(crop_y)
                        crop_width = float(crop_width)
                        crop_height = float(crop_height)
                    except ValueError:
                        return render(request, 'upload.html', {'error': 'Invalid cropping coordinates'})

                    # Open the uploaded photo using Pillow
                    image = Image.open(photo_path)

                    # Calculate the cropping region
                    left = int(crop_x)
                    top = int(crop_y)
                    right = int(crop_x + crop_width)
                    bottom = int(crop_y + crop_height)

                    # Crop the image
                    cropped_image = image.crop((left, top, right, bottom))

                    # Save the cropped image as the profile picture
                    cropped_photo_path = 'rootmedia/profile_images/i' + str(CurrentUser.userid) + '.' + file_extension
                    cropped_image.save(cropped_photo_path)

                    # Remove the temporary uploaded photo
                    os.remove(photo_path)
                    CurrentDesign = Design()
                    return render(request, 'settings/settings.html', {
                        'page': 'settings',
                        'cuser': CurrentUser,
                        'design': CurrentDesign,
                    })
                else:
                    return JsonResponse({}, status=400)
            else:
                return JsonResponse({}, status=400)
        else:
            return JsonResponse({}, status=400)
    return JsonResponse({}, status=400)


# def logout(request):
#     """Provides users the ability to logout (func)"""
#     return HttpResponseRedirect('/')


class MainLogoutView(LogoutView):
    """Provides users the ability to logout (class)"""
    next_page = '/'