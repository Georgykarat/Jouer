# Generated by Django 4.2.1 on 2023-05-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_customuser_city_alter_customuser_cordinates_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangePasswordRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=30)),
                ('reqtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
