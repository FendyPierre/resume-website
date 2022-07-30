from django.urls import path, include, re_path
from core.views import HomeView

app_name = 'core'

urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
]