from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path(r'', views.IndexView.as_view(), name="index"),
    re_path(r'^(?P<pk>\d+)$', views.PostDetailView.as_view(), name="post-detail")
]