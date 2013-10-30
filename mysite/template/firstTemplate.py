__author__ = 'renfei'

from django import template
from django.http import HttpResponse
from django.conf import settings
settings.configure()


def  useTemplate(request):
    dt = "user the template"
    html = "<html><body> %s </html></body>" % dt
    return HttpResponse(html)


def  templateOne():
    t = template.Template("my name is {{ name }}")
    print t
    c = template.Context({"name":"renfei"})
    print t.render(c)


templateOne()
