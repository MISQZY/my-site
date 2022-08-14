from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('news/', include('news.urls')),
    path('storage/', include('my_storage.urls')),
]

handler404="main.views.error404"
handler500="main.views.error500"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
