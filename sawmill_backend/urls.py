"""
URL configuration for sawmill_backend project.

This file routes URLs to their corresponding views.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import core views
from core.views import index_view, admin_html, save_content

urlpatterns = [
    # Default Django admin panel
    path('admin/', admin.site.urls),

    # API endpoints from the core app
    path('api/', include('core.urls')),

    # Homepage view (renders index.html)
    path('', index_view, name='index'),

    # Custom admin UI page (HTML)
    path('admin.html', admin_html, name='admin_html'),

    # API to save site content dynamically
    path('api/content/', save_content, name='save_content'),
]

# Serve media and static files during development
if settings.DEBUG:
    # Serve uploaded media files (images, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Serve static files (CSS, JS, etc.)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
