from django.conf.urls import url

from views import Meetings, MeetingNew


urlpatterns = [
    url(r'^$', Meetings.as_view(), name='meetings'),
    url(r'^new/$', MeetingNew.as_view(), name='meeting-new'),
]
