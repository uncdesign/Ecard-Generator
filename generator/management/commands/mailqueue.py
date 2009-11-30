from django.core.management.base import NoArgsCommand
from generator.models import Card, Picture, Bow, Typeface
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import Template, Context, loader
from settings import SITE_URL

class Command(NoArgsCommand):
	def handle_noargs(self, **options):
		unsentcards = Card.objects.filter(sent=False).order_by("timestamp")[:2]
		#template = loader.get_template("card.html")
		for card in unsentcards:
			#print template.render(Context({"card":card}))
			print render_to_string('card.html', locals())
			baseurl = SITE_URL
			print render_to_string('card.txt', locals())
			card.sent = True
			card.save()
		return '\n'.join(['%s %s' % (k.timestamp, k.hashid) for k in unsentcards]).encode('utf-8')
		
		
		

"""subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
text_content = 'This is an important message.'
html_content = '<p>This is an <strong>important</strong> message.</p>'
msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
msg.attach_alternative(html_content, "text/html")
msg.send()
return render_to_response("confirm.html", locals())"""