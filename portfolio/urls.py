from django.urls import path
from portfolio.views import HomeView, SendMail, ProjectDetail, ProjectAPI

app_name = "portfolio"

urlpatterns = [
    path('', HomeView, name='home'),
    path('send-mail/', SendMail, name="send_mail"),
    path('project-details', ProjectDetail, name="project_detail"),
    path('api/v1/projects', ProjectAPI.as_view(), name='api_projects')
]