from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework.renderers import JSONRenderer
from works_single_view.models import Work
from works_single_view.api.serializers import WorkSerializer


class WorkViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows works to be viewed.
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    def list(self, request, *args, **kwargs):
        iswc_str = request.data.get('iswc')
        if iswc_str:
            iswc_list = iswc_str.split(',')
            works_list = Work.objects.filter(iswc__in=iswc_list)
        else:
            works_list = Work.objects.all()[:10]

        data = [self.prep_work(work) for work in works_list]
        context = {'data': data}

        return Response(data=context)

    def prep_work(self, data):
        contributors = [cont.name for cont in data.contributors.all()]
        doc = {
            'iswc': data.iswc,
            'title': data.title,
            'contributors': contributors
        }
        return doc
