
from django.db import models
from multiselect.fields import ManyToManyField

class Choice(models.Model):
    choice = models.CharField(max_length=15)

    def __unicode__(self):
        return self.choice

class SampleModel(models.Model):
    name = models.CharField(max_length=15)
    choices = ManyToManyField(Choice)
    passwd = models.TextField()
    def __unicode__(self):
        return unicode(self.pk)