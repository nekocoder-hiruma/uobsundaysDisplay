from django.conf.urls import patterns, url, include

from .views import YoungArtistOverviewView, YoungArtistSubmissionView, YoungArtistSubmissionDetailVoteView, YoungArtistWinnersView, \
    YoungArtistWinnersDetailView

urlpatterns = patterns('',
                       url(r'^submissions/$', YoungArtistSubmissionView.as_view(), name='submission'),
                       url(r'^$', YoungArtistOverviewView.as_view(), name='index'),
                       url(r'^(?P<pk>[0-9]+)/$', YoungArtistSubmissionDetailVoteView.as_view(), name='submission_vote'),
                       url(r'^winners/', include([
                           url(r'^$', YoungArtistWinnersView.as_view(), name='winners'),
                           url(r'^(?P<pk>[0-9]+)/$', YoungArtistWinnersDetailView.as_view(),
                               name='winners-detail'),
                       ]))
                       )
