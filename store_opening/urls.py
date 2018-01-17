from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.store_opening, name="store_opening")
]
