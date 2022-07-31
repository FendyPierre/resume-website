from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from resume_website.storage import PublicMediaStorage
from utils.image import resize_public_image

User = get_user_model()
# Create your models here.


class BaseModelClass(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DoingText(BaseModelClass):
    text = models.TextField()
    title = models.CharField(max_length=250, blank=True, null=True)
    icon = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'resume_doing'
        verbose_name_plural = 'What Im doing texts'
        ordering = ['text']

    def __str__(self):
        return self.title


class Profile(BaseModelClass):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    github = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    csv_path = models.CharField(max_length=255, blank=True, null=True)
    favicon_path = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    doings = models.ManyToManyField(DoingText)

    class Meta:
        db_table = 'resume_profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class University(BaseModelClass):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'resume_university'
        verbose_name_plural = 'universities'
        ordering = ['name']

    def __str__(self):
        return self.name


class Education(BaseModelClass):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    degree = models.CharField(max_length=500)
    major = models.CharField(max_length=500)
    minor = models.CharField(max_length=500, blank=True, null=True)
    gpa = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'resume_education'
        verbose_name_plural = 'education degrees'
        ordering = ['start_date']

    def __str__(self):
        return f'{self.university.name} - {self.degree} - {self.major}/{self.minor if self.major else ""}'


class Project(BaseModelClass):
    name = models.CharField(max_length=255)
    brief_description = models.CharField(max_length=500, null=True, blank=True)
    repo = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, storage=PublicMediaStorage())
    description = models.TextField()
    backend = models.CharField(max_length=250, null=True, blank=True)
    frontend = models.CharField(max_length=250, null=True, blank=True)
    platform = models.CharField(max_length=250, null=True, blank=True)
    database = models.CharField(max_length=250, null=True, blank=True)
    mobile = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'resume_project'
        verbose_name_plural = 'projects'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resize_public_image(image=self.image, crop=False)


class WorkHistoryTask(BaseModelClass):
    description = models.CharField(max_length=500)

    class Meta:
        db_table = 'resume_work_history_task'
        verbose_name_plural = 'resume work history tasks'
        ordering = ['description']

    def __str__(self):
        return self.description


class WorkHistory(BaseModelClass):
    company = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    technologies = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    tasks = models.ManyToManyField(WorkHistoryTask)

    class Meta:
        db_table = 'resume_work_history'
        verbose_name_plural = 'work histories'
        ordering = ['-start_date']

    def __str__(self):
        return self.title


class Skills(BaseModelClass):
    name = models.CharField(max_length=255)
    proficiency = models.IntegerField()

    class Meta:
        db_table = 'resume_skills'
        verbose_name_plural = 'skills'
        ordering = ['name']

    def __str__(self):
        return self.name


class SkillsSet(BaseModelClass):
    name = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skills)

    class Meta:
        db_table = 'resume_skill_set'
        verbose_name_plural = 'skill sets'
        ordering = ['name']

    def __str__(self):
        return self.name


class ImageCategory(BaseModelClass):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'resume_image_category'
        verbose_name_plural = 'image categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class GalleryImage(BaseModelClass):
    name = models.CharField(max_length=255)
    image = models.ImageField(storage=PublicMediaStorage())
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'resume_image'
        verbose_name_plural = 'images'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resize_public_image(image=self.image, crop=False)


class VisitWebRequestHistory(BaseModelClass):
    host = models.CharField(max_length=1000)
    user_agent = models.CharField(max_length=1000, blank=True, null=True)
    path = models.CharField(max_length=1000, blank=True, null=True)
    remote_address = models.GenericIPAddressField()
    remote_address_fwd = models.GenericIPAddressField(blank=True, null=True)
    is_secure = models.BooleanField()
    is_ajax = models.BooleanField()
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    meta = models.JSONField()
    cookies = models.JSONField()
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'resume_visit'
        verbose_name_plural = 'visits'
        ordering = ['created_date', 'host', 'remote_address']

    def __str__(self):
        return f'{self.created_date} - {self.host} - {self.remote_address} - {self.user}'
