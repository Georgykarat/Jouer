from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.conf import settings
from django.utils import timezone
from home.forms import AuthForm
from home.models import SignUpModel, CustomUser, ChangePasswordRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.text import MIMEText
from django.contrib.auth.hashers import make_password
from email import encoders
import random
import string


# Functions for views
def is_ajax(request):
    """Function to check if request is ajax
    Args:
        request ([request]): [just request via url]
    Returns:
        [bool]: [True if request is ajax]
    """
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def code_generate(l):
    """Function to generate random code
    Args:
        l (int): [length of code]
    Returns:
        [str]: [random code]
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(l))
    
    """
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(l))

def send_email(addr_to, msg_subj, msg_text):
    """
    Function to send mail from Jouer mail
    Args:
        addr_to ([str]): [mail to]
        msg_subj ([str]): [subject of mail]
        msg_text ([str]): [text of mail. Code was already generated]
    Returns:
        [None]: [None]
    
    """
    addr_from = settings.MAIL_REGCONF
    password = settings.MAIL_REGCONF_PASSWORD

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = msg_subj

    body = msg_text
    msg.attach(MIMEText(body, 'plain'))

    #Mail provider settings
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.ehlo()
    #server.starttls()
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()

# Views

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


def signin(request, *args, **kwargs):
    """Function to render login page
    Args:
        request ([request]): [just request via url]
    Returns:
        [render func]: [render login page]
    """
    if request.user.is_authenticated == True:
        return HttpResponseRedirect('/feed/')
    else:
        if request.method == 'POST':
            auth_form = AuthForm(request.POST, label_suffix='')
            if auth_form.is_valid():
                mail = auth_form.cleaned_data['mail']
                password = auth_form.cleaned_data['password']
                user = authenticate(username=mail.lower(), password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/feed/')
                    else:
                        auth_form.add_error('__all__', 'Erroe! An account is inactive!')
                else:
                    auth_form.add_error('__all__', 'Login or password incorrect')
        else:
            auth_form = AuthForm()
        context = {
            'form': auth_form
        }
        return render(request, 'home/signin.html', context=context)

def generate_confcode(request):
    """
    The function generates mail confirmation code and sends it to the user
    Args:
        request ([request]): [just request via url]
    Returns:
        [JsonResponse]: [Json with status 200]
    
    """
    if is_ajax(request=request):
        mail_to_reg = request.POST['mail'].lower()
        code = code_generate(6)
        regcode = 'Your code is ' + code
        testuser = SignUpModel.objects.filter(mail=mail_to_reg)
        # We need to check, if the code was generated in the last 10 minutes
        if testuser:
            if SignUpModel.objects.filter(mail=mail_to_reg).values_list('timestamp')[0][0] <= timezone.now() - timezone.timedelta(minutes=10):
                testuser.delete()
                tempuser = SignUpModel(mail=mail_to_reg, code=code)
                tempuser.save()
                send_email(mail_to_reg, 'Registration code', regcode)
            else:
                pass
                # Here we can return a page "Code has been already requested"
        else:
            tempuser = SignUpModel(mail=mail_to_reg, code=code)
            tempuser.save()
            send_email(mail_to_reg, 'Registration code', regcode)
        return JsonResponse({}, status=200)
    

def check_code(request):
    """
    The function checks the code and if it is correct, the user is redirected to the main page
    Args:
        request ([request]): [just request via url]
    Returns:
        [JsonResponse]: [Json with status 200]
    
    """
    if is_ajax(request=request):
        mail_to_reg = request.POST['mail'].lower()
        code_to_reg = request.POST['code'].lower()
        password = request.POST['password']
        testuser = SignUpModel.objects.filter(mail=mail_to_reg)
        if testuser:
            if (testuser.values_list('code')[0][0]).lower() == code_to_reg:
                testuser.delete()
                varhash = make_password(password, None, 'pbkdf2_sha1')
                newuser = User(username=mail_to_reg.lower(), password=varhash)
                newuser.save()
                newuser = CustomUser(user=newuser, email=mail_to_reg.lower())
                newuser.save()
                login(request, newuser)
                return JsonResponse({}, status=200)
            else:
                return JsonResponse({}, status=400)
        else:
            return JsonResponse({}, status=400)
        


def changepass(request):
    """
    The function checks the confirmation code and generates anew one, if it is not exist
    Args:
        request ([request]): [just request via url]
    Returns:
        [JsonResponse]: [Json with status 200]
    """
    if is_ajax(request=request):
        mail_to_recover = request.POST['mail'].lower()
        OurUser = User.objects.filter(username=mail_to_recover) # !!! Here we need to check user in Users table
        if OurUser:
            ConfCode = SignUpModel(mail=mail_to_recover)
            if ConfCode:
                # If Mail Confirmation code exists in db
                if SignUpModel.objects.filter(mail=mail_to_recover).values_list('timestamp')[0][0] <= timezone.now() - timezone.timedelta(minutes=10):
                    # There is old code (+10m.) - generate and send a new code
                    ConfCode.delete()
                    code = code_generate(6)
                    ConfCode = SignUpModel(mail=mail_to_recover, code=code)
                    ConfCode.save()
                    send_email(mail_to_recover, 'Your password recovery code:', code)
                    return JsonResponse({}, status=200)
                else:
                    # There is a code which was generated in the last 10 minutes - just to resend it
                    send_email(mail_to_recover, 'Your password recovery code:', ConfCode.values_list('code')[0][0])
                    return JsonResponse({}, status=200)
            else:
                # if Mail Confirmation code does not exist in db - create code and send mail
                code = code_generate(6)
                ConfCode = SignUpModel(mail=mail_to_recover, code=code)
                ConfCode.save()
                send_email(mail_to_recover, 'Your password recovery code:', code)
                return JsonResponse({}, status=200)
        else:
            return JsonResponse({}, status=400)
    else:
        return JsonResponse({}, status=400)
    

def checkcode(request):
    if is_ajax(request=request):
        mail_to_recover = request.POST['mail'].lower()
        code_to_check = request.POST['approve_code']
        ConfCode = SignUpModel(mail=mail_to_recover, code=code_to_check)
        if ConfCode:
            if SignUpModel.objects.filter(mail=mail_to_recover, code=code_to_check).values_list('timestamp')[0][0] <= timezone.now() - timezone.timedelta(minutes=10):
                returndata = {'reason':"Code has expired"}
                return JsonResponse(returndata, status=400)
            else:
                change_password_code = code_generate(50)
                encrypted_object = ChangePasswordRequest(mail=mail_to_recover,code=change_password_code)
                encrypted_object.save()
                returndata = {'encrypted_code':change_password_code}
                return JsonResponse(returndata, status=200)
        else:
            return JsonResponse({}, status=400)
    else:
            return JsonResponse({}, status=400)
    

def setnewpassword(request):
    if is_ajax(request=request):
        mail_to_recover = request.POST['mail'].lower()
        code_to_check = request.POST['requestcode']
        new_password = request.POST['new_password']
        encrypted_object = ChangePasswordRequest.objects.filter(mail=mail_to_recover,code=code_to_check)
        if encrypted_object:
            encrypted_object.delete()
            varhash = make_password(new_password, None, 'pbkdf2_sha1')
            User.objects.filter(username=mail_to_recover).update(password=varhash)
            return JsonResponse({}, status=200)
        else:
            return JsonResponse({}, status=400)
    else:
        return JsonResponse({}, status=400)
