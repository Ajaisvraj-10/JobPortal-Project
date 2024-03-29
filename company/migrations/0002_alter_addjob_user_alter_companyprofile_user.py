# Generated by Django 4.2.1 on 2023-07-15 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_customuser_can_login_and_more'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addjob',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.company'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.company'),
        ),
    ]
