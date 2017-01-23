from django.conf.urls import url

from views import MeetingNew


urlpatterns = [
    url(r'^meetings/new/$', MeetingNew.as_view(), name='meeting-new'),
]
