from django.urls import path, include, re_path
from django.contrib.auth.views import login, logout
from . import views

app_name = 'about'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="index"),
    re_path(r'^login/', login, {'template_name': 'about/login.html'}),
    re_path(r'^logout/', logout, {'template_name': 'about/logout.html'}),
]