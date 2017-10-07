from rest_framework.routers import DefaultRouter

from app.services.viewsets import ServiceViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)