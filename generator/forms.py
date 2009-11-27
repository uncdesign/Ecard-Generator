from django.forms import ModelForm
from generator.models import Card

class CreateCardForm(ModelForm):
	class Meta:
		model = Card
		fields = ['toemail', 'fromemail', 'message', 'typeface', 'picture', 'bow']