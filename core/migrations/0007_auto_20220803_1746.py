# Generated by Django 3.2.14 on 2022-08-03 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile_receive_notifications'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doingtext',
            options={'ordering': ['ordering'], 'verbose_name_plural': 'What Im doing texts'},
        ),
        migrations.AddField(
            model_name='doingtext',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]