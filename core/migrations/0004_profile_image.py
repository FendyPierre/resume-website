# Generated by Django 3.2.14 on 2022-07-31 20:37

from django.db import migrations, models
import resume_website.storage


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_visitwebrequesthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=resume_website.storage.PublicMediaStorage(), upload_to=''),
        ),
    ]
