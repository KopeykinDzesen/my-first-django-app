from django.urls import path, include
from . import views

urlpatterns = [
    path('basket_adding/', views.basket_adding, name="basket_adding"),
    path('delete_product_in_basket/', views.delete_product_in_basket, name="delete_product_in_basket"),
    path('checkout/', views.checkout, name="checkout"),
]