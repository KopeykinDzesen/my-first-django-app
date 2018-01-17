from django.conf.urls import url
from django.urls import path, include
from products import views

urlpatterns = [
    path('', views.product, name='product'),
]