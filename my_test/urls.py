from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.my_test, name="my_test"),
]