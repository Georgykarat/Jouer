# Generated by Django 4.2.1 on 2023-05-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_alter_boardgamesbase_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgamesbase',
            name='iconpath',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='boardgamesbase',
            name='imagepath',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
