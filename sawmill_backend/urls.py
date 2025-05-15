"""
URL configuration for sawmill_backend project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import index_view, admin_html, save_content

urlpatterns = [
    path('admin/', admin.site.urls),                     # Django admin
    path('api/', include('core.urls')),                  # API routes from core/urls.py
    path('', index_view, name='index'),                  # Homepage view
    path('admin.html', admin_html, name='admin_html'),   # Custom admin HTML page
    path('api/content/', save_content, name='save_content'),  # API to save content
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   # Serve static files (e.g., admin CSS/JS)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
