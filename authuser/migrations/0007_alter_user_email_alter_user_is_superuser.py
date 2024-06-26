# Generated by Django 5.0.6 on 2024-05-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0006_alter_user_email_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
