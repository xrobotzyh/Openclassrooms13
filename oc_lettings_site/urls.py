from django.contrib import admin
from django.urls import path, include

from . import settings
from .views import index, page_404, page_500
from django.contrib.staticfiles.urls import static


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = page_404
handler500 = page_500
