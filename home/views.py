from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.conf import settings
from django.utils import timezone
from home.models import SignUpModel
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.text import MIMEText
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

    print(addr_from, password)

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


def login(request, *args, **kwargs):
    """Function to render login page
    Args:
        request ([request]): [just request via url]
    Returns:
        [render func]: [render login page]
    """
    return render(request, 'home/login.html', {
    })

def generate_confcode(request):
    if is_ajax(request=request):
        mail_to_reg = request.POST['mail'].lower()
        code = code_generate(6)
        regcode = 'Your code is ' + code
        send_email(mail_to_reg, 'Registration code', regcode)
        testuser = SignUpModel.objects.filter(mail=mail_to_reg)
        if testuser:
            testuser.delete()
        tempuser = SignUpModel(mail=mail_to_reg, code=code)
        tempuser.save()
        return JsonResponse({}, status=200)