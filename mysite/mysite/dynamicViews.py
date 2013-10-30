__author__ = 'renfei'

from django.http import HttpResponse,Http404
import datetime

def currentDateTime(request):
    now = datetime.datetime.now()
    date = datetime.date.max
    datetimes = datetime.datetime
    html = "<html><body> now %s. </br> date %s</html></body>" % (now,date)
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
