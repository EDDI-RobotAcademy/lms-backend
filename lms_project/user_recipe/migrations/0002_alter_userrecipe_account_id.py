# Generated by Django 5.0.7 on 2024-09-09 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_accountattendancecheck_attendance_last_login_month'),
        ('user_recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrecipe',
            name='account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
    ]