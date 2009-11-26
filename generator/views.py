from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from generator.models import Card, Picture, Bow, Typeface
from base64 import urlsafe_b64encode, urlsafe_b64decode
# Create your views here.

def displaycard(request, cardid):
	card = get_object_or_404(Card, id=cardid)
	return render_to_response('displaycard.html', locals())
	
def displaycardhash(request, cardid):
	try:
		cardid = urlsafe_b64decode(str(cardid))
	except TypeError:
		raise Http404()
	card = get_object_or_404(Card, id=cardid)
	return render_to_response('displaycard.html', locals())