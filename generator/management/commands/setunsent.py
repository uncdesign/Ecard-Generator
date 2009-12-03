from django.core.management.base import NoArgsCommand
from generator.models import Card

class Command(NoArgsCommand):
	def handle_noargs(self, **options):
		sentcards = Card.objects.filter(sent=True).order_by("timestamp")
		for card in sentcards:
			card.sent = False
			card.save()
		return '\n'.join(['%s %s' % (k.timestamp, k.hashid) for k in sentcards]).encode('utf-8')
