from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from generator.models import Card, Picture, Bow, Typeface
from generator.forms import CreateCardForm
import random
# Create your views here.

def displaycard(request, cardid):
	card = get_object_or_404(Card, id=cardid)
	return render_to_response('displaycard.html', locals())
	
def displaycardhash(request, cardid):
	card = get_object_or_404(Card, hashid=cardid)
	return render_to_response('displaycard.html', locals())
	
def createcard(request):
	form = CreateCardForm()
	if request.method == 'POST':
		form = CreateCardForm(request.POST)
		if form.is_valid():
			new_card = form.save(commit=False)
			random.seed()
			hash = random.getrandbits(128)
			new_card.hashid = str(hash)
			new_card.save()
			## do something.
	else:
		form = CreateCardForm()
	return render_to_response("createcard.html", { "form": form,})
	
	
	#return render_to_response('createcard.html', locals())