from django.conf.urls.defaults import *
from django.conf import settings
from settings import SITE_ROOT
import os
from generator.views import displaycard, displaycardhash, createcard


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^ecardgenerator/', include('ecardgenerator.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^create/$', createcard),
    
	('', include('generator.urls')),
)

