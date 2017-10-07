from rest_framework import serializers

from app.services.models import ServiceDescription, Service


class ServiceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDescription
        fields = ['name', 'cover', 'description', 'sort_index']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'cover', 'short_description', 'sort_index']


class ServiceDetailSerializer(serializers.ModelSerializer):
    service_desces = ServiceDescriptionSerializer(many=True)

    class Meta:
        model = Service
        fields = ['id', 'name', 'cover', 'service_desces']