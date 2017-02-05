import pytz

from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from forms import MeetingForm
from models import Meeting


class Meetings(ListView):
    model = Meeting

    def get_context_data(self, **kwargs):
        context = super(Meetings, self).get_context_data(**kwargs)
        context['common_timezones'] = pytz.common_timezones
        context['timezone'] = self.request.GET.get('timezone') or settings.TIME_ZONE
        return context


class MeetingNew(CreateView):
    model = Meeting
    form_class = MeetingForm

    def form_valid(self, form):
        date_time = self.request.POST['datetime']
        time_zone = self.request.POST['timezone'] or settings.TIME_ZONE
        date_time_format = '%m/%d/%y %H:%M'
        naive_datetime_obj = datetime.strptime(date_time, date_time_format)
        form.instance.datetime = pytz.timezone(time_zone).localize(naive_datetime_obj)
        return super(MeetingNew, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(MeetingNew, self).get_context_data(**kwargs)
        context['common_timezones'] = pytz.common_timezones
        return context

    def get_success_url(self):
        messages.success(self.request, 'Meeting posted.')
        return reverse('meeting-new')
