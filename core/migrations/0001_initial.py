# Generated by Django 3.2.14 on 2022-07-30 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoingText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('icon', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'What Im doing texts',
                'db_table': 'resume_doing',
                'ordering': ['text'],
            },
        ),
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'image categories',
                'db_table': 'resume_image_category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('brief_description', models.CharField(blank=True, max_length=500, null=True)),
                ('repo', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
                ('backend', models.CharField(blank=True, max_length=250, null=True)),
                ('frontend', models.CharField(blank=True, max_length=250, null=True)),
                ('platform', models.CharField(blank=True, max_length=250, null=True)),
                ('database', models.CharField(blank=True, max_length=250, null=True)),
                ('mobile', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'projects',
                'db_table': 'resume_project',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('proficiency', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'skills',
                'db_table': 'resume_skills',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'universities',
                'db_table': 'resume_university',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WorkHistoryTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'resume work history tasks',
                'db_table': 'resume_work_history_task',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('company', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('technologies', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('tasks', models.ManyToManyField(to='core.WorkHistoryTask')),
            ],
            options={
                'verbose_name_plural': 'work histories',
                'db_table': 'resume_work_history',
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='SkillsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('skills', models.ManyToManyField(to='core.Skills')),
            ],
            options={
                'verbose_name_plural': 'skill sets',
                'db_table': 'resume_skill_set',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('github', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('csv_path', models.CharField(blank=True, max_length=255, null=True)),
                ('favicon_path', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('doings', models.ManyToManyField(to='core.DoingText')),
            ],
            options={
                'verbose_name_plural': 'profiles',
                'db_table': 'resume_profile',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.imagecategory')),
            ],
            options={
                'verbose_name_plural': 'images',
                'db_table': 'resume_image',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('degree', models.CharField(max_length=500)),
                ('major', models.CharField(max_length=500)),
                ('minor', models.CharField(blank=True, max_length=500, null=True)),
                ('gpa', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.university')),
            ],
            options={
                'verbose_name_plural': 'education degrees',
                'db_table': 'resume_education',
                'ordering': ['start_date'],
            },
        ),
    ]
