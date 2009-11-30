from django.db import models
from django.forms import ModelForm, ModelChoiceField, EmailField
from django.forms.widgets import RadioSelect
from generator.models import Card, Picture, Bow, Typeface

class CreateCardForm(ModelForm):
	toemail = EmailField(required=True)
	fromemail = EmailField(required=True)
	picture = ModelChoiceField(widget=RadioSelect, queryset=Picture.objects.all(), required=True, empty_label=None)
	typeface = ModelChoiceField(widget=RadioSelect, queryset=Typeface.objects.all(), required=True, empty_label=None)
	bow = ModelChoiceField(widget=RadioSelect, queryset=Bow.objects.all(), required=True, empty_label=None)
	
	
	class Meta:
		model = Card
		fields = ['picture', 'bow', 'message', 'typeface', 'toemail', 'fromemail', 'fromname']