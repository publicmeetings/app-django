from django.conf.urls import url

from views import Meetings, MeetingNew


urlpatterns = [
    url(r'^meetings/$', Meetings.as_view(), name='meetings'),
    url(r'^meetings/new/$', MeetingNew.as_view(), name='meeting-new'),
]
