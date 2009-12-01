from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from generator.models import Card, Picture, Bow, Typeface
from generator.forms import CreateCardForm
from settings import MEDIA_URL
import random
# Create your views here.

def displaycard(request, cardid):
	card = get_object_or_404(Card, id=cardid)
	return render_to_response('displaycard.html', locals())
	
def displaycardhash(request, cardid):
	card = get_object_or_404(Card, hashid=cardid)
	return render_to_response('displaycard.html', locals())
	
def createcard(request):
	picture_list = Picture.objects.all()
	typeface_list = Typeface.objects.all()
	bow_list = Bow.objects.all()
	form = CreateCardForm()
	mediaurl = MEDIA_URL
	if request.method == 'POST':
		form = CreateCardForm(request.POST)
		if form.is_valid():
			new_card = form.save(commit=False)
			random.seed()
			hash = random.getrandbits(128)
			new_card.hashid = str(hash)
			new_card.save()
			return render_to_response("confirm.html", locals())
			## do something.
	else:
		form = CreateCardForm()
	return render_to_response("createcard.html", locals())
	
	
def stats(request):
	cards_unsent = Card.objects.filter(sent=False).count()
	cards_in_db = Card.objects.count()
	lastest_card = Card.objects.latest('id')
	cards_total = lastest_card.id
	cards_sent = cards_total - cards_unsent
	return render_to_response("stats.html", locals())