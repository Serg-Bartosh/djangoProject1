# Generated by Django 5.0.2 on 2024-03-05 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
    ]
