from rest_framework import viewsets

from app.services.models import Service
from app.services.serializers import ServiceSerializer, ServiceDetailSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ServiceDetailSerializer
        return super(ServiceViewSet, self).get_serializer_class()

    # def get_queryset(self):
    #     return Service.objects.filter(active=True)