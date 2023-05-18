from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import offers_list, page_admin, add_promotion

urlpatterns = [

    path('', offers_list, name='offers_list'),
    path('admin/', page_admin, name='page_admin'),
    path('add_promotion/<int:product_id>/', add_promotion, name='add_promotion'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
