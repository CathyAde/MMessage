# Generated by Django 4.2 on 2024-09-19 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='username',
            new_name='nom',
        ),
        migrations.RemoveField(
            model_name='member',
            name='full_name',
        ),
    ]
