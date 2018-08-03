from django.urls import path, include, re_path
from . import views

app_name = 'contact'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name="index"),
]