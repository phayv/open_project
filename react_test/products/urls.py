from django.urls import path, re_path
from . import views

app_name = 'Products'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="index"),
    re_path(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product-detail'),
]
