from django.urls import path, include
from .views import ApplicationViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'applications', ApplicationViewSet)




urlpatterns = [
    path('api/', include(router.urls)),
]
# Not Found: /serverinfo/api/upload/
