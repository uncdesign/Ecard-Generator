from django.core.management.base import NoArgsCommand
from generator.models import Card, Picture, Border, Typeface
from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import Template, Context, loader
from settings import *

class Command(NoArgsCommand):
	"""Send unsent emails in the database, then set emails to sent=true"""
	def handle_noargs(self, **options):
		unsentcards = Card.objects.filter(sent=False).filter(spam=False).order_by("timestamp")[:35] #Get the oldest unsent emails
		for card in unsentcards:		
			baseurl = SITE_URL
			subject = "You've received a Carolina ecard from %s" % card.fromname
			from_email, to = "holiday@uncgreetings.org", card.toemail
			text_content = render_to_string('card.txt', locals())
			html_content = render_to_string('card.html', locals())
			msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			try:
				msg.send()
			except SMTPRecipientsRefused:
				card.spam = True
				card.save()
			else:
				card.sent = True
				card.save()
		return '\n'.join(['id: %s spam: %s time: %s hash id: %s sent: %s' % (k.id, k.spam, k.timestamp, k.hashid, k.sent) for k in unsentcards]).encode('utf-8')