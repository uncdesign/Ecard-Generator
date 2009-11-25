from django.shortcuts import render_to_response
from generator.models import Card, Picture, Bow, Typeface

# Create your views here.

def displaycard(request, cardid):
	card = Card.objects.get(id=cardid)
	return render_to_response('displaycard.html', locals())
	
