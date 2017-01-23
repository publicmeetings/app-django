from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Meeting(BaseModel):
    title = models.CharField(max_length=255)
    topic = models.TextField()
    link = models.URLField()
    datetime = models.DateTimeField()

    # tmp
    organization = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
