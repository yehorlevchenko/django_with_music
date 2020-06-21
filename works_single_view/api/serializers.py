from works_single_view.models import Work, Contributor
from rest_framework.serializers import ModelSerializer


class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = ['iswc', 'title', 'contributors']


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['name']