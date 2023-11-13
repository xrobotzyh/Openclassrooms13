from django.contrib import admin
from django.urls import path, include

from .views import index, page_404, page_500

urlpatterns = [
    path('', index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
handler404 = page_404
handler500 = page_500
