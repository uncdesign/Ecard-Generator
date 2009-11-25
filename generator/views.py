from django.shortcuts import render_to_response, get_object_or_404
from generator.models import Card, Picture, Bow, Typeface

# Create your views here.

def displaycard(request, cardid):
	card = get_object_or_404(Card, id=cardid)
	return render_to_response('displaycard.html', locals())
	
