from django.db import models
from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import RadioSelect
from generator.models import Card, Picture, Bow, Typeface
#from generator.widgets import *

class CreateCardForm(ModelForm):
	picture = ModelChoiceField(widget=RadioSelect, queryset=Picture.objects.all(), required=True, empty_label=None)
	typeface = ModelChoiceField(widget=RadioSelect, queryset=Typeface.objects.all(), required=True, empty_label=None)
	bow = ModelChoiceField(widget=RadioSelect, queryset=Bow.objects.all(), required=True, empty_label=None)
	
	
	class Meta:
		model = Card
		fields = ['toemail', 'fromemail', 'message', 'typeface', 'picture', 'bow']