from django.contrib import admin

from models import Meeting


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'organization', 'datetime', 'location', 'link')


admin.site.register(Meeting, MeetingAdmin)
