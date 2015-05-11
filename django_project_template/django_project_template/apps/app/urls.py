from django.conf.urls.static import static
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from apps.app.views import *

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^/?$','apps.app.views.index',name='index'),
)