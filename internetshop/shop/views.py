from django.shortcuts import render

# Create your views here.


class HttpResponse:
    pass


def home(request):
    return HttpResponse("Даровы это сайт артёма")