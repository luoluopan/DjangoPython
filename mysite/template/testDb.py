__author__ = 'renfei'

from django.db import models
from django.conf import settings
settings.configure()


class Test(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    website = models.URLField()
    date = models.DateField()


def test():
#    t = Test(name='renfei',age=12,website='http://weibo.com/renfeiluoluo')
#    t.save()
    print("test===========")

test()

