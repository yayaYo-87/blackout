from rest_framework import serializers

from app.mainpage.models import TopSlide, BottomSlide, Slider


class TopSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopSlide
        fields = ['id', 'name', 'cover', 'description', 'ikon', 'link']


class BottomSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomSlide
        fields = ['id', 'name', 'cover', 'description', 'link']


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'name',]


class SliderDetaileSerializer(serializers.ModelSerializer):
    bottom_sliders = BottomSlideSerializer(many=True, required=False)
    top_sliders = TopSlideSerializer(many=True, required=False)

    class Meta:
        model = Slider
        fields = ['id', 'name', 'top_sliders', 'bottom_sliders']