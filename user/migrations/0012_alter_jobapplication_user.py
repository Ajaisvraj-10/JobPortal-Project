# Generated by Django 4.2.1 on 2023-07-11 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_customuser_can_login_and_more'),
        ('user', '0011_alter_jobapplication_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.user'),
        ),
    ]
