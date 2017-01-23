from django.shortcuts import render
from django.views.generic.edit import CreateView

from models import Meeting


class MeetingNew(CreateView):
    model = Meeting
    fields = ('title', 'topic', 'link', 'organization', 'location', 'datetime')
