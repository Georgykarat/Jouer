# Generated by Django 4.2.1 on 2023-05-24 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_boardgamesbase_iconpath_boardgamesbase_imagepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgamesbase',
            name='rusname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='boardgamesbase',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
