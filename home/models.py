from django.db import models

# Create your models here.


class SignUpModel(models.Models):
    mail = models.EmailField()
    code = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)