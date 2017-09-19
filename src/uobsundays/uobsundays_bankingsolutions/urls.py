from django.conf.urls import patterns, url
from .views import BankingSolutionsListView

urlpatterns = patterns('',
                       url(r'^$', BankingSolutionsListView.as_view(), name='bankingsolutions'),
                       )
