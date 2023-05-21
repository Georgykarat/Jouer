from django.contrib import admin
from .models import BoardgamesBase

# Register your models here.

@admin.register(BoardgamesBase)
class BoardgamesBaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'min_players', 'max_players', 'min_age', 'category', 'complexity')
    search_fields = ('name', 'category')