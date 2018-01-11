# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *
urlpatterns = [
    url('^$', ServicesView.as_view(), name='services'),
    url('^shares/$', HomeView.as_view(), name='shares'),
    url('^prices/$', PricesView.as_view(), name='prices'),
    url('^contacts/$', ContactsView.as_view(), name='contacts'),
    url('^sauna/(?P<slug>[a-z_\-0-9]+)/$', SaunaView.as_view(), name='sauna'),
]
