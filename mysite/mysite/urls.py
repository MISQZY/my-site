from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls'), name= 'home'),
    path('storage/', include('my_storage.urls')),
    path('user/', include('user.urls'))
]

handler404="news.views.handle_not_found"

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls')),] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
