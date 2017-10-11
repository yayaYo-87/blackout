from rest_framework import viewsets

from app.devices.serializers import ProjectCategorySerializer, ProjectCategoryDetailSrializer, ProjectSerializer, \
    ProjectDetailSerializer
from app.projects.models import ProjectCategory, Project


class ProjectCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectCategoryDetailSrializer
        return super(ProjectCategoryViewSet, self).get_serializer_class()


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return super(ProjectViewSet, self).get_serializer_class()


class ResentProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return super(ProjectViewSet, self).get_serializer_class()

    def get_queryset(self):
        return Project.objects.filter(resent=True)
