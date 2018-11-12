from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^client/', include('pysy_client.urls', namespace='pysy_client', app_name='pysy_client')),
    url(r'^api/', include('pysy_api.urls', namespace='pysyy', app_name='pysyy')),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

