from django.urls import path, include
from .views import inventory, ServerViewSet, ServerroleViewSet, EnvironmentViewSet, RegionViewSet, ZoneViewSet
from .views import OrganizationViewSet, ProjectViewSet, AppidViewSet, CountryViewSet, SubnetSerializer

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'servers', ServerViewSet)
router.register(r'serverroles', ServerroleViewSet)
router.register(r'environments', EnvironmentViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'zones', ZoneViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'appids', AppidViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'subnets', SubnetSerializer)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', inventory.as_view(), name='inventory')
]
# Not Found: /serverinfo/api/upload/

