from django.contrib import admin
from uobsundays_youngartist.models import YoungArtistOverview, YoungArtistSubmission, YoungArtistWinner


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('artist', 'image', 'likes', 'created', 'age', 'location')
    list_filter = ('location',)

    ordering = ('-created',)

admin.site.register(YoungArtistOverview)
admin.site.register(YoungArtistSubmission, SubmissionAdmin)
admin.site.register(YoungArtistWinner)
