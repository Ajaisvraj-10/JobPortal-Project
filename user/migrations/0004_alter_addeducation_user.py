# Generated by Django 4.2.1 on 2023-06-17 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_rename_user_profile_addeducation_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addeducation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]