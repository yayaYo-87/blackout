from rest_framework import viewsets

from app.devices.serializers import ProjectCategorySerializer, ProjectCategoryDetailSerializer, ProjectSerializer, \
    ProjectDetailSerializer
from app.projects.models import ProjectCategory, Project


class ProjectCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectCategoryDetailSerializer
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
        return super(ResentProjectViewSet, self).get_serializer_class()

    def get_queryset(self):
        return Project.objects.filter(resent=True)


class MainProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return super(MainProjectViewSet, self).get_serializer_class()

    def get_queryset(self):
        return Project.objects.filter(is_main=True)
