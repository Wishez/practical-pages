from django.conf.urls import url
from .views import *
urlpatterns = [
    url('^$', HomePage.as_view(), name='home'),
]