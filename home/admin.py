from django.contrib import admin
from home.models import SignUpModel, CustomUser, ChangePasswordRequest

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ['mail','code','timestamp']
    search_fields = ['mail','code']


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email','access', 'verified']
    search_fields = ['user','email']


class ChangePasswordRequestAdmin(admin.ModelAdmin):
    list_display = ['mail', 'reqtime']
    search_fields = ['mail']



admin.site.register(SignUpModel,SignUpAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(ChangePasswordRequest,ChangePasswordRequestAdmin)