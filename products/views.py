from django.shortcuts import render
from .models import Product, ProductImage


def product(request, product_id):

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    product = Product.objects.get(id=product_id)
    images_product = ProductImage.objects.filter(product__id=product_id)
    image0 = images_product[0].image
    image1 = images_product[1].image
    image2 = images_product[2].image

    products_images_this_category = ProductImage.objects.filter(is_active=True, is_main=True,
                            product__is_active=True, product__category__id=product.category.id)
    if len(products_images_this_category) > 4:
        products_images_this_category = products_images_this_category[4:]

    return render(request, 'products/product.html', locals())
