from django.urls import path
from . import views

urlpatterns = [
    path("facebook/", views.facebook, name='facebook'),
    path("mecanics/", views.mecanics, name='mecanics'),
    path("mathematics/", views.mathematics, name='mathematics'),
    path("english/", views.english, name='english'),
    path("french/", views.french, name='french'),
]