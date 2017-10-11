from rest_framework import viewsets

from app.mainpage.models import Slider
from app.mainpage.serializers import SliderSerializer, SliderDetaileSerializer


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SliderDetaileSerializer
        return super(SliderViewSet, self).get_serializer_class()