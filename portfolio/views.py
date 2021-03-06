from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProjectSerializer, ImageSerializer
from .models import Project, Images
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics 
from rest_framework import mixins 

def HomeView(request, *args, **kwargs):
    django_projects = Project.objects.filter(primary_framework='Django')
    all_projects = Project.objects.all()
    express_projects = Project.objects.filter(primary_framework='Express')
    vue_projects = Project.objects.filter(primary_framework='Vue')
    
    context = {
        'all_projects': all_projects,
        'vue_projects': vue_projects,
        'django_projects': django_projects,
        'express_projects': express_projects
    }
    return render(request, 'index.html', context)

def ProjectDetail(request, project_id, project_slug, *args, **kwargs):
    project = Project.objects.filter(slug=project_slug).get(pk=project_id)
    context = {
        'Project': project
    }
    print(project)
    return render(request, 'portfolio-details.html', context)

def SendMail(request, *args, **kwargs):
    if not request.method == "POST":
        return HttpResponseRedirect(reverse('portfolio:home'))
    if request.method == "POST":
        subject = request.POST['subject']
        message = f"""
        Mail From: {request.POST['email']},
        {request.POST['message']}
        """
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]
    
    try:
        send_mail(subject, message, email_from, recipient_list)
        return render(request, "thank-you.html", {
            "message": "Mail Successfully Sent!"
        })
    except Exception  as e:
        return render(request, "thank-you.html", {
            "error": e
        })


class ProjectAPI(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):

    # permission_classes = (IsAuthenticated, )

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

class ImagesAPI(APIView):
    def get(self, request, project_id, project_slug, *args, **kwargs):
        project = Project.objects.filter(slug=project_slug).get(pk=project_id)
        qs = project.images_set.all()
        serializer = ImageSerializer(qs, many=True)
        return Response(serializer.data)


def page_not_found_404(request, exception):
    return render(request, '404.html', status=404)

