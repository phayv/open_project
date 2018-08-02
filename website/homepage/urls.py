from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name="index"),
]