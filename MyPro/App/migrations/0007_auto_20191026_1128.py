# Generated by Django 2.1.12 on 2019-10-26 11:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20191026_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='failed_login_attemts',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Failure Attempts'),
        ),
    ]