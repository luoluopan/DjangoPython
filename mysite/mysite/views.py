__author__ = 'renfei'

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world !")


