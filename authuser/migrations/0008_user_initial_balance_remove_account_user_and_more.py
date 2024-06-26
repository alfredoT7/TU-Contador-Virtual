# Generated by Django 5.0.6 on 2024-05-27 21:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0007_alter_user_email_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='initial_balance',
            field=models.FloatField(default=0.0),
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
