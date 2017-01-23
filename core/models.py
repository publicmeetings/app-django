from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Meeting(BaseModel):
    title = models.CharField(max_length=255)
    topic = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    datetime = models.DateTimeField()

    # tmp
    organization = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255)
