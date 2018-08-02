from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path(r'', views.IndexView.as_view(), name="index"),
]