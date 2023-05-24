from django.db import models

# Create your models here.


class BoardgamesBase(models.Model):
    name = models.CharField(max_length=100)
    rusname = models.CharField(max_length=100, blank=True)
    year = models.IntegerField()
    min_players = models.IntegerField(blank=True)
    max_players = models.IntegerField(blank=True)
    min_age = models.IntegerField(blank=True)
    category = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    complexity = models.IntegerField(blank=True)
    playtimeminutes = models.IntegerField(blank=True)
    genre_competitive = models.BooleanField(blank=True)
    genre_cooperative = models.BooleanField(blank=True)
    genre_campaign = models.BooleanField(blank=True)
    is_dlc = models.BooleanField(default=False)
    base_game = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='dlcs')
    imagepath = models.CharField(max_length=200, blank=True)
    iconpath = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name