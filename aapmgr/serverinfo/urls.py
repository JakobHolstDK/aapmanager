# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetViewSet, ServerViewSet, upload_json, asset_list, server_list, server_info


router = DefaultRouter()
router.register(r'assets', AssetViewSet)
router.register(r'servers', ServerViewSet)

urlpatterns = [
    path('/api/', include(router.urls)),
    path("/api/upload-json/", upload_json, name='upload-json'),  # New endpoint for JSON upload
    path("/assets/", asset_list),  # New endpoint for listing assets
    path("/servers/", server_list),  # New endpoint for listing servers
    path("/servers/<pk>", server_info)  # New endpoint for listing servers
]
# Not Found: /serverinfo/api/upload/
