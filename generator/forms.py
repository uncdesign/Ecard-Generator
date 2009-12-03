from django.db import models
from django.forms import ModelForm, ModelChoiceField, EmailField, CharField
from django.forms.widgets import RadioSelect, Textarea
from generator.models import Card, Picture, Border, Typeface

class CreateCardForm(ModelForm):
	toemail = EmailField(required=True, max_length=255)
	fromemail = EmailField(required=True, max_length=255)
	picture = ModelChoiceField(widget=RadioSelect, queryset=Picture.objects.all(), required=True, empty_label=None)
	typeface = ModelChoiceField(widget=RadioSelect, queryset=Typeface.objects.all(), required=True, empty_label=None)
	border = ModelChoiceField(widget=RadioSelect, queryset=Border.objects.all(), required=True, empty_label=None)
	message = CharField(widget=Textarea, required=True, max_length=230)
	
	class Meta:
		model = Card
		fields = ['picture', 'border', 'message', 'typeface', 'toemail', 'fromemail', 'fromname']