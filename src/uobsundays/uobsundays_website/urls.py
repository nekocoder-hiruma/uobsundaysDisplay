from django.conf.urls import patterns, url
from .views import IndexView, LocateUsView, SignUpView

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^locate-us/$', LocateUsView.as_view(), name='locate_us'),
                       url(r'^sign-up/$', SignUpView.as_view(), name='sign_up'),
                       )
