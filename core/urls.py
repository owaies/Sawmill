from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index_view,SiteContentViewSet, login_view, admin_panel_view,  save_content

router = DefaultRouter()
router.register(r'content', SiteContentViewSet)

urlpatterns = [
    path('', index_view, name='index'),
    path('api/', include(router.urls)),
    path('login/', login_view, name='login'),
    path('admin-panel/', admin_panel_view, name='admin_panel'),
    path('api/content/', save_content, name='save_content'),
]
