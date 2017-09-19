from django.conf.urls import patterns, url, include
from uobsundays_event.views import *

urlpatterns = patterns('',
                       url(r'^june/$', EventOverviewTemplateView.as_view(), name='index'),
                       url(r'^july/$', EventOverviewTemplateView2.as_view(), name='index2'),
                       url(r'^june/gallery/', include([
                           url(r'^$', EventImagesListView.as_view(), name='gallery'),
                           url(r'^latest/$', EventImagesLatestListView.as_view(), name='latestgallery'),
                           url(r'^oldest/$', EventImagesReverseListView.as_view(), name='oldestgallery')
                       ])),
                       url(r'^july/gallery/', include([
                            url(r'^$', EventImagesJulyListView.as_view(), name='gallery2'),
                            url(r'^latest/$', EventImagesJulyLatestListView.as_view(), name='latestgallery2'),
                            url(r'^oldest/$', EventImagesJulyReverseListView.as_view(), name='oldestgallery2')
                       ])),
                       url(r'^november/gallery/', include([
                            url(r'^$', EventImagesNovemberListView.as_view(), name='gallery3'),
                            url(r'^latest/$', EventImagesNovemberLatestListView.as_view(), name='latestgallery3'),
                            url(r'^oldest/$', EventImagesNovemberReverseListView.as_view(), name='oldestgallery3')
                       ])),
                       )
