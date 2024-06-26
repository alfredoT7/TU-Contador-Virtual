# Generated by Django 5.0.6 on 2024-05-27 21:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0008_user_initial_balance_remove_account_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category_type', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='initial_balance',
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authuser.category'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ManyToManyField(related_name='user_account', to=settings.AUTH_USER_MODEL),
        ),
    ]
