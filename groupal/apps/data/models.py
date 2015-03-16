from django.db import models

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.name
