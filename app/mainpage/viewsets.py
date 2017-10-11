from rest_framework import viewsets

from app.mainpage.models import TopSlider, BottomSlider
from app.mainpage.serializers import TopSliderSerializer, BottomSliderSerializer


class TopSliderViewSet(viewsets.ModelViewSet):
    queryset = TopSlider.objects.all()
    serializer_class = TopSliderSerializer


class BottomSliderViewSet(viewsets.ModelViewSet):
    queryset = BottomSlider.objects.all()
    serializer_class = BottomSliderSerializer