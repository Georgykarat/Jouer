from django.db import models
from django.contrib.auth.models import User
from encrypted_model_fields.fields import EncryptedCharField

# Create your models here.


class SignUpModel(models.Model):
    mail = models.EmailField()
    code = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)


class CustomUser(models.Model):
    REQUIRED_FIELDS = ('user',)
    USERNAME_FIELD = 'user'

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    cordinates = models.CharField(max_length=50, null=True, blank=True)
    access = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    image_path = models.CharField(verbose_name="image path", max_length = 1000, blank=True)


class ChangePasswordRequest(models.Model):
    """
    Model to store codes for change pass requests (used to request change password from login page)
    """
    mail = models.EmailField()
    code = EncryptedCharField(max_length=40)
    reqtime =  models.DateTimeField(auto_now_add=True)