from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from photo import settings

urlpatterns = [
    path('config_admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('price/', include('price.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

