# Generated by Django 4.2.1 on 2023-06-10 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addproject',
            old_name='user',
            new_name='user_profile',
        ),
        migrations.RenameField(
            model_name='addskills',
            old_name='name',
            new_name='skill_name',
        ),
    ]
