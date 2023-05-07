from django.contrib import admin
from home.models import SignUpModel, CustomUser

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ['mail','code','timestamp']
    search_fields = ['mail','code']


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email','access', 'verified']
    search_fields = ['user','email']




admin.site.register(SignUpModel,SignUpAdmin)
admin.site.register(CustomUser,CustomUserAdmin)