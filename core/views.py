import json
import socket
import geoip2.database

import os
from geoip2.errors import AddressNotFoundError
from django.conf import settings
from django.http import JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.generic import View, TemplateView, DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.core.mail import send_mail
from django.utils.timezone import now
from core.models import (
    Project, SkillsSet, WorkHistory,
    Education, ImageCategory, GalleryImage,
    Profile, User, VisitWebRequestHistory
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
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        # store session

        def dumps(value):
            return json.dumps(value, default=lambda o: None)

        if hasattr(request, 'user'):
            user = request.user if isinstance(request.user, User) else None
        else:
            user = None

        meta = request.META.copy()
        meta.pop('QUERY_STRING', None)
        meta.pop('HTTP_COOKIE', None)
        remote_addr_fwd = None

        if 'HTTP_X_FORWARDED_FOR' in meta:
            remote_addr_fwd = meta['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
            if remote_addr_fwd == meta['HTTP_X_FORWARDED_FOR']:
                meta.pop('HTTP_X_FORWARDED_FOR')
        remote_addr = meta.pop('REMOTE_ADDR', None)
        user_agent = meta.pop('HTTP_USER_AGENT', None)
        meta = {} if not meta else dumps(meta)
        cookies = {} if not request.COOKIES else dumps(request.COOKIES)

        # get location of ip address
        location = 'Location Unavailable'
        location_raw = location
        if remote_addr_fwd:
            ip = remote_addr_fwd.split(',')[0]
        elif remote_addr:
            ip = remote_addr.split(',')[0]
        else:
            ip = None
        if ip:
            # check if ip address is valid
            try:
                socket.inet_aton(ip)
                ip_valid = True
            except socket.error:
                ip_valid = False
        else:
            ip_valid = False
        if ip_valid:
            path = os.path.join(settings.BASE_DIR, 'static', 'geo_location', 'GeoLite2-City.mmdb')
            with geoip2.database.Reader(path) as reader:
                try:
                    response = reader.city(ip)
                    location = f'{response.country}, {response.city}'
                    location_raw = response.raw
                except AddressNotFoundError:
                    pass
        if not request.session:
            request.session.create()
        session = Session.objects.filter(session_key=request.session.session_key).first()
        qs = VisitWebRequestHistory.objects.filter(session=session, created_date__year=now().year)
        if not qs.exists():
            # send email and store session
            VisitWebRequestHistory(
                host=request.get_host(),
                path=request.path,
                user_agent=user_agent,
                remote_address=remote_addr,
                remote_address_fwd=remote_addr_fwd,
                is_secure=request.is_secure(),
                is_ajax=request.is_ajax(),
                user=user,
                meta=meta,
                cookies=cookies,
                session=session,
                location=location
            ).save()
            send_mail(
                from_email=settings.SERVER_EMAIL,
                subject=f'New Visitor from {location}',
                message=location_raw if location_raw else '',
                recipient_list=[settings.SERVER_EMAIL],
                fail_silently=False
            )
        return response


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
                send_mail(
                    subject=f'New message from {email}',
                    message=message,
                    from_email=settings.SERVER_EMAIL,
                    recipient_list=[settings.SERVER_EMAIL],
                    fail_silently=False
                )
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

