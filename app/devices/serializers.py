from rest_framework import serializers

from app.projects.models import ProjectCategory, Project, ProjectImage
from app.devices.models import Producer, Category, SubCategory, Devices
from app.projects.models import ProjectDevice
from app.projects.serializers import ProjectCategorySerializer


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['id', 'name', 'cover', 'country']


class DevicesSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer()

    class Meta:
        model = Devices
        fields = [
            'id',
            'name',
            'cover',
            'tag',
            'producer',
        ]


class SubCategorySerializer(serializers.ModelSerializer):
    device_subcategories = DevicesSerializer(many=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'device_subcategories']


class CategorySerializer(serializers.ModelSerializer):
    cat_subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'cover', 'short_desc', 'cat_subcategories']


class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'cover', 'short_desc', ]


class DevicesDetailSerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer()
    producer = ProducerSerializer()
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Devices
        fields = [
            'id',
            'name',
            'cover',
            'is_main',
            'sort_index',
            'tag',
            'sub_category',
            'producer',
            'producer_link',
            'projects',
            'description',
        ]





class ProjectImageSerializer(serializers.Serializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image']


class ProjectDeviceSerializer(serializers.Serializer):
    category = CategorySerializer()
    device = DevicesSerializer(many=True)

    class Meta:
        model = ProjectDevice
        fields = ['id', 'category', 'device']


class ProjectDetailSerializer(serializers.Serializer):
    category = ProjectCategorySerializer()
    project_devices = ProjectDeviceSerializer(many=True)
    project_images = ProjectImageSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'cover', 'description', 'youtube_link', 'resent', 'category', 'project_devices', 'project_images']


class ProjectCategoryDetailSrializer(serializers.Serializer):
    project_categories = ProjectSerializer(many=True)

    class Meta:
        model = ProjectCategory
        fields = ['id', 'name', 'project_categories']
