from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from generator.models import Card, Picture
from generator.forms import *
import random
from settings import *
# Create your views here.

def displaycard(request, cardid):
	"""Display a card in the database via id"""
	baseurl = SITE_URL
	card = get_object_or_404(Card, id=cardid)
	return render_to_response('displaycard.html', locals())
	
def displaycardhash(request, cardid):
	"""Display a card in the database via hash id"""
	baseurl = SITE_URL
	card = get_object_or_404(Card, hashid=cardid)
	return render_to_response('displaycard.html', locals())
	
def createcard(request):
	"""Ecard creator form"""
	
	# Get the options from the db
	picture_list = Picture.objects.all()
	
	# Create Form from models
	form = CreateCardForm()
	
	# If data has been submitted check validity
	if request.method == 'POST': 
		form = CreateCardForm(request.POST)
		#Save card if it's valid
		if form.is_valid():
			new_card = form.save(commit=False)
			
			#Generate random id
			random.seed() 
			hash = random.getrandbits(128)
			new_card.hashid = str(hash)
			new_card.ipaddress = request.META.get('REMOTE_ADDR')
			
			new_card.save()
			return render_to_response("confirm.html", locals())
	else:
		form = CreateCardForm()
	return render_to_response("createcard.html", locals())
	
	
def stats(request):
	"""Show card statistics"""
	cards_unsent = Card.objects.filter(sent=False).filter(spam=False).count()
	cards_spam = Card.objects.filter(spam=True).count()
	cards_in_db = Card.objects.count()
	lastest_card = Card.objects.latest('id')
	cards_total = lastest_card.id
	cards_sent = cards_total - cards_unsent - cards_spam
	return render_to_response("stats.html", locals())