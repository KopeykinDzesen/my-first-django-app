from django.shortcuts import render
from products.models import ProductImage


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_iPhones = products_images.filter(product__category__id=4)
    products_images_MacBooks = products_images.filter(product__category__id=5)
    products_images_iPad = products_images.filter(product__category__id=6)
    if len(products_images) > 4:
        products_images = products_images[4:]
    return render(request, 'landing/home.html', locals())
