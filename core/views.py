from django.shortcuts import render
from django.views.generic.edit import CreateView

from forms import MeetingForm
from models import Meeting


class MeetingNew(CreateView):
    model = Meeting
    form_class = MeetingForm
