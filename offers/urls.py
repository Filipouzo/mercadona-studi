from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import offers_list, product_create, page_admin

urlpatterns = [

    path('', offers_list, name='offers_list'),
    path('form/', product_create, name='product_form'),
    path('admin/', page_admin, name='page_admin'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

