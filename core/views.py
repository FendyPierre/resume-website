from django.http import JsonResponse, FileResponse, HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.generic import View, TemplateView, DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from core.models import (
    Project, SkillsSet, WorkHistory,
    Education, ImageCategory, GalleryImage,
    Profile
)


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['project_list'] = Project.objects.all()
        context['education_list'] = Education.objects.all()
        context['skills_set_list'] = SkillsSet.objects.all()
        context['work_list'] = WorkHistory.objects.all()
        context['category_list'] = ImageCategory.objects.all()
        context['image_list'] = GalleryImage.objects.all()
        context['profile'] = Profile.objects.first()
        print(context['skills_set_list'])
        return context


class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(csrf_exempt, name='dispatch')
class SendMessageView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if not all([name, email, message]):
            try:
                validate_email(email)
                # TODO: configure email and send message.
                response = {
                    'success': 1,
                    'message': 'success'
                }
            except ValidationError:
                response = {
                    'success': 0,
                    'message': 'fill form completely'
                }
        else:

            response = {
                'success': 1,
                'message': 'success'
            }
        return JsonResponse(response)

