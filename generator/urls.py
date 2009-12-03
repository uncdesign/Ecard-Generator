from django.conf.urls.defaults import *
from django.conf import settings
from settings import SITE_ROOT
import os
from generator.views import displaycard, displaycardhash, createcard, stats

urlpatterns = patterns('',

    (r'^$', createcard),
    
    (r'^card/(?P<cardid>.*)/$', displaycardhash), # Display a stored card via the hash id
    
    (r'^stats/$', stats), # Display card generator stats
    
)

# If Django is in debug mode, allow these URLS to be visible
if settings.LOCALHOST:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(SITE_ROOT, 'generator/static')}),
	)