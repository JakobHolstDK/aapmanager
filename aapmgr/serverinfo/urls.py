# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetViewSet, upload_json, asset_list, server_list

router = DefaultRouter()
router.register(r'assets', AssetViewSet)

urlpatterns = [
    path('/api', include(router.urls)),
    path("/api/upload-json", upload_json, name='upload-json'),  # New endpoint for JSON upload
    path("/assets", asset_list),  # New endpoint for listing assets
    path("/servers", server_list)  # New endpoint for listing servers
]
# Not Found: /serverinfo/api/upload/
