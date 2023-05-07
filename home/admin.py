from django.contrib import admin
from home.models import SignUpModel

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ['mail','code','timestamp']
    search_fields = ['mail','code']




admin.site.register(SignUpModel,SignUpAdmin)