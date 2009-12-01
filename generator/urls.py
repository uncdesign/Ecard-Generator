from django.conf.urls.defaults import *
from django.conf import settings
from settings import SITE_ROOT
import os
from generator.views import displaycard, displaycardhash, createcard

urlpatterns = patterns('',

    (r'^create/$', createcard),
    
    (r'^card/(?P<cardid>.*)/$', displaycardhash), 
    
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(SITE_ROOT, 'images')}),
		(r'^cardid/(?P<cardid>\d+)/', displaycard),
	)