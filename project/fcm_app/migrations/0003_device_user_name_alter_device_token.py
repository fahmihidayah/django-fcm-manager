# Generated by Django 4.0.6 on 2022-08-02 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcm_app', '0002_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='user_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='token',
            field=models.TextField(default='', max_length=2000),
        ),
    ]
