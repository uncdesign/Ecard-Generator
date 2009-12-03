from django.conf.urls.defaults import *
from django.conf import settings
import os
from generator.views import displaycard, displaycardhash, createcard, stats

urlpatterns = patterns('',

    (r'^create/$', createcard), # Card Creator
    
    (r'^$', createcard),
    
    (r'^card/(?P<cardid>.*)/$', displaycardhash), # Display a stored card via the hash id
    
    (r'^stats/$', stats), # Display card generator stats
    
)

# If Django is in debug mode, allow these URLS to be visible
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^cardid/(?P<cardid>\d+)/', displaycard),
	)