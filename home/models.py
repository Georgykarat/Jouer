from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SignUpModel(models.Model):
    mail = models.EmailField()
    code = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)


class CustomUser(models.Model):
    REQUIRED_FIELDS = ('user',)
    USERNAME_FIELD = 'user'

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    status = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    cordinates = models.CharField(max_length=50, null=True)
    access = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)
    image_path = models.CharField(verbose_name="image path", max_length = 1000, blank=True)