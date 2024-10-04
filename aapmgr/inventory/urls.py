from django.urls import path, include
from .views import inventory, ServerViewSet, ServerroleViewSet, EnvironmentViewSet, RegionViewSet, ZoneViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'servers', ServerViewSet)
router.register(r'serverroles', ServerroleViewSet)
router.register(r'environments', EnvironmentViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'zones', ZoneViewSet)



urlpatterns = [
    path('api', include(router.urls)),
    path('', inventory.as_view(), name='inventory')
]
# Not Found: /serverinfo/api/upload/

