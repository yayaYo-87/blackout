from rest_framework import serializers

from app.devices.models import Producer, Category, SubCategory


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['id', 'name', 'cover', 'country']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'cover', 'short_desc']


class SubCategorySerializer(serializers.ModelSerializer):
    cat_subcategories = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'cat_subcategories']


class DevicesCategory(serializers.ModelSerializer):
    device_subcategories = SubCategorySerializer()

    class Meta