# Generated by Django 2.1.12 on 2019-11-05 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_auto_20191105_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to='App.Organization'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to='App.Role'),
        ),
    ]