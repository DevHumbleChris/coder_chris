from django.urls import path
from portfolio.views import HomeView, SendMail, ProjectApi

app_name = "portfolio"

urlpatterns = [
    path('', HomeView, name='home'),
    path('send-mail/', SendMail, name="send_mail"),
    path('api/v1/', ProjectApi.as_view(), name="project_api"),
]