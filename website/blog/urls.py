from django.urls import path, include, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="index"),
    re_path(r'^(?P<pk>\d+)$', views.PostDetailView.as_view(), name="post-detail")
]