from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store_opening/', include('store_opening.urls')),
    path('my_test/', include('my_test.urls')),
    path('', include('landing.urls')),
    path('orders/', include('orders.urls')),
    path('product/<product_id>/', include('products.urls'), name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
