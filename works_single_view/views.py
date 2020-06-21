from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import reverse

from .models import Work, Contributor
from .utils import parse_works, save_works


def index(request):
    template = loader.get_template('index.html')
    if request.method == 'GET':
        works_list = Work.objects.all()
        context = {'works_list': works_list}
        return HttpResponse(template.render(context, request))
    else:
        in_file = request.FILES.get('csv_file')
        if not in_file:
            return HttpResponseRedirect(reverse('index'))

        if in_file.name.endswith('.csv'):
            data = in_file.read().decode('utf-8')
            raw_works_list = parse_works(data)
            save_works(raw_works_list)

        return HttpResponseRedirect(reverse('index'))
