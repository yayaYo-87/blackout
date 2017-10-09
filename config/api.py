from rest_framework.routers import DefaultRouter

from app.devices.viewsets import CategoryViewSet, DevicesViewSet
from app.projects.viewsets import ProjectViewSet, ProjectCategoryViewSet
from app.services.viewsets import ServiceViewSet

router = DefaultRouter()
router.register(r'service', ServiceViewSet)

router.register(r'devices_category', CategoryViewSet)
router.register(r'device', DevicesViewSet)

router.register(r'project_category', ProjectCategoryViewSet)
router.register(r'project', ProjectViewSet)