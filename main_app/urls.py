from django.urls import path,include
from . import views

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path('notify', views.notify, name="notify"),
    path('team', views.team, name="team"),
    path('trial2', views.trial2, name="trial2"),
]
