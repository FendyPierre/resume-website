# Generated by Django 3.2.14 on 2022-08-02 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220731_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='receive_notifications',
            field=models.BooleanField(default=False),
        ),
    ]
