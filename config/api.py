from rest_framework.routers import DefaultRouter

from app.devices.viewsets import CategoryViewSet, DevicesViewSet
from app.mainpage.viewsets import TopSliderViewSet, BottomSliderViewSet
from app.projects.viewsets import ProjectCategoryViewSet, ProjectViewSet
from app.services.viewsets import ServiceViewSet

router = DefaultRouter()
router.register(r'service', ServiceViewSet)

router.register(r'devices_category', CategoryViewSet)
router.register(r'device', DevicesViewSet)

router.register(r'project_category', ProjectCategoryViewSet)
router.register(r'project', ProjectViewSet)

router.register(r'top_sliders', TopSliderViewSet)
router.register(r'bottom_sliders', BottomSliderViewSet)