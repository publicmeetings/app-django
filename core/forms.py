from django import forms

from models import Meeting


class MeetingForm(forms.ModelForm):
    link = forms.URLField(initial='http://', required=False)
    datetime = forms.DateTimeField(help_text='mm/dd/yy hh:mm', label='Date and time')

    class Meta:
        model = Meeting
        fields = ('title', 'topic', 'link', 'organization', 'location', 'datetime')
