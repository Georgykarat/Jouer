# Generated by Django 4.2.1 on 2023-05-21 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardgamesBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField(max_length=4)),
                ('min_players', models.IntegerField(blank=True)),
                ('max_players', models.IntegerField(blank=True)),
                ('min_age', models.IntegerField(blank=True)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('complexity', models.IntegerField(blank=True)),
                ('playtimeminutes', models.IntegerField(blank=True)),
                ('genre_competitive', models.BooleanField(blank=True)),
                ('genre_cooperative', models.BooleanField(blank=True)),
                ('genre_campaign', models.BooleanField(blank=True)),
                ('is_dlc', models.BooleanField(default=False)),
                ('base_game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dlcs', to='feed.boardgamesbase')),
            ],
        ),
    ]