
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


from .views import index, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_view, name='login'),
    path('offers/', include("offers.urls")),
    path('', index, name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)