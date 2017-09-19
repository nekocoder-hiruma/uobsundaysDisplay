"""UOBSundays URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^', include('uobsundays_website.urls',
                                         app_name='website',
                                         namespace='website')),
                       url(r'^events/', include('uobsundays_event.urls',
                                                app_name='events',
                                                namespace='events')),
                       url(r'^bankingsolutions/', include('uobsundays_bankingsolutions.urls',
                                                          app_name='bankingsolutions',
                                                          namespace='bankingsolutions')),
                       url(r'^littleartcontest/', include('uobsundays_youngartist.urls',
                                                     app_name='youngartist',
                                                     namespace='youngartist')),
                       (r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
                       url(r'', include('social.apps.django_app.urls', namespace='social')),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
                       url(r'^imagefit/', include('imagefit.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'google72a925ed082e67c2\.html ', TemplateView.as_view(template_name='google72a925ed082e67c2.html'))
                       ) + static(r'media', document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

