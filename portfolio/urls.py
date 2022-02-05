from django.urls import path
from portfolio.views import HomeView, SendMail, ProjectDetail, ProjectAPI, ImagesAPI

app_name = "portfolio"

urlpatterns = [
    path('', HomeView, name='home'),
    path('send-mail/', SendMail, name="send_mail"),
    path('project-details/<int:project_id>/<slug:project_slug>/', ProjectDetail, name="project_detail"),
    path('api/v1/projects', ProjectAPI.as_view(), name='api_projects'),
    path('api/v1/projects/<int:project_id>/<slug:project_slug>', ImagesAPI.as_view(), name='images_api')
]