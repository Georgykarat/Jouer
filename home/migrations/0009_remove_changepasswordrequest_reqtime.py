# Generated by Django 4.2.1 on 2023-05-21 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_changepasswordrequest_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='changepasswordrequest',
            name='reqtime',
        ),
    ]
