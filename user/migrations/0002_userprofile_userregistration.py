# Generated by Django 4.2.1 on 2023-05-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('cont_email', models.EmailField(max_length=254)),
                ('cont_phone', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('skills', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('experience', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]