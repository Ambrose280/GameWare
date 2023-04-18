
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include("eshop.urls")),
    path('admin/', admin.site.urls),
    path('auth/', include("authentication.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
