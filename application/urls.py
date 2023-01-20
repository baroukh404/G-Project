from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path(r'home/', views.home, name='home'),
	path(r'contact/', views.sendsms, name='contact'),
	path(r'login/', views.login, name='login'),
	# path(r'test/', views.test, name='test'),
]


# path(r'home/<int:year>', views.home),
# path(r'home/<str:name>', views.home, name='home'),
# path(r'home/<float:value>', views.home, name='home'),