from django.urls import path
from portfolio.views import HomeView

urlpatterns = [
    path('', HomeView, name='home')
]