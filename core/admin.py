from django.contrib import admin
from core.models import (
    Project, WorkHistory, Skills, SkillsSet,
    WorkHistoryTask, GalleryImage, ImageCategory,
    Education, University, Profile, DoingText, VisitWebRequestHistory
)
# Register your models here.


admin.site.register([
    Project, WorkHistory, Skills, SkillsSet, WorkHistoryTask,
    GalleryImage, ImageCategory, Education, University, Profile,
    DoingText, VisitWebRequestHistory
])

