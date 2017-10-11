from rest_framework import viewsets

from app.devices.models import Devices, Category
from app.devices.serializers import DevicesSerializer, DevicesDetailSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DevicesViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DevicesDetailSerializer
        return super(DevicesViewSet, self).get_serializer_class()
