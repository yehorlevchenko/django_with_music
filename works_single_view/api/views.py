from rest_framework import viewsets
from works_single_view.models import Work, Contributor
from works_single_view.api.serializers import (
    WorkSerializer,
    ContributorSerializer
)


class WorkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class ContributorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
