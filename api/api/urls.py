# api/urls.py
from django.contrib import admin
from django.urls import path, include        # add this
from django.conf import settings             # add this
from django.conf.urls.static import static   # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('core.urls'))       # add this
]

# add this
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)