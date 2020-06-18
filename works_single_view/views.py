from django.http import HttpResponse


def index(request):
    return HttpResponse("Music single view app")