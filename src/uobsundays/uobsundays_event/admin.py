from django.contrib import admin
from uobsundays_event.models import EventImage, EventImage2, EventImage3


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'created')

    ordering = ('-created',)

admin.site.register(EventImage, EventAdmin)
admin.site.register(EventImage2, EventAdmin)
admin.site.register(EventImage3, EventAdmin)
