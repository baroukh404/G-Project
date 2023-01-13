from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.users, name='users'),
    path("mecanics/", views.mecanics, name='mecanics'),
    path("mathematics/", views.mathematics, name='mathematics'),
    path("english/", views.english, name='english'),
    path("french/", views.french, name='french'),
]