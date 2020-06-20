from works_single_view.models import Work, Contributor
from rest_framework import serializers


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['iswc', 'title', 'contributors']


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['name']