from django.urls import path, include, re_path
from core.views import HomeView, ProjectDetailView, SendMessageView

app_name = 'core'

urlpatterns = [
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail_view'),
    path('send_message', SendMessageView.as_view(), name='send_message_view'),
    re_path(r'^$', HomeView.as_view(), name='home_view'),
]