# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *
urlpatterns = [
    url('^$', HomeView.as_view(), name='home'),
    url('^services/$', ServicesView.as_view(), name='services'),
    url('^prices/$', PricesView.as_view(), name='prices'),
    url('^contacts/$', ContactsView.as_view(), name='contacts'),
    url('^sauna/(?P<slug>[a-z_]+)/$', SaunaView.as_view(), name='sauna'),
]