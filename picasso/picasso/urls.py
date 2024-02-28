
from django.contrib import admin
from django.urls import path
from fileflow.views import FileViewSet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('files/', FileViewSet.as_view({'get': 'list'})),
    path('upload/', FileViewSet.as_view({'post': 'create'})),  
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
