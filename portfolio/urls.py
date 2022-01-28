from django.urls import path
from portfolio.views import HomeView, SendMail

app_name = "portfolio"

urlpatterns = [
    path('', HomeView, name='home'),
    path('send-mail/', SendMail, name="send_mail")
]