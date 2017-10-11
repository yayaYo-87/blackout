from rest_framework import serializers

from app.mainpage.models import TopSlide, BottomSlide, TopSlider, BottomSlider


class TopSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopSlide
        fields = ['id', 'name', 'cover', 'description', 'ikon', 'link']


class BottomSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomSlide
        fields = ['id', 'name', 'cover', 'description', 'link']


class TopSliderSerializer(serializers.ModelSerializer):
    top_sliders = TopSlideSerializer(many=True, required=False)

    class Meta:
        model = TopSlider
        fields = ['id', 'name', 'top_sliders']


class BottomSliderSerializer(serializers.ModelSerializer):
    bottom_sliders = BottomSlideSerializer(many=True, required=False)

    class Meta:
        model = BottomSlider
        fields = ['id', 'name', 'bottom_sliders']