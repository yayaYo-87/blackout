from app.devices import serializers
from app.projects.models import ProjectCategory


class ProjectCategorySerializer(serializers.Serializer):
    class Meta:
        model = ProjectCategory
        fields = ['id', 'name', 'cover', 'short_desc']