from django.urls import path, include, re_path
from django.contrib.auth.views import login, logout
from . import views

app_name = 'about'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name="index"),
    path(r'login/', login, {'template_name': 'about/login.html'}),
    path(r'logout/', logout, {'template_name': 'about/logout.html'}),
]