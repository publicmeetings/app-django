from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from forms import MeetingForm
from models import Meeting


class Meetings(ListView):
    model = Meeting


class MeetingNew(CreateView):
    model = Meeting
    form_class = MeetingForm

    def get_success_url(self):
        messages.success(self.request, 'Meeting saved.')
        return reverse('meeting-new')
