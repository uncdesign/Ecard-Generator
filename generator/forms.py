from django.db import models
from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import RadioSelect
from generator.models import Card, Picture, Bow, Typeface

class CreateCardForm(ModelForm):
	picture = ModelChoiceField(widget=RadioSelect, queryset=Picture.objects.all())
	typeface = ModelChoiceField(widget=RadioSelect, queryset=Typeface.objects.all())
	bow = ModelChoiceField(widget=RadioSelect, queryset=Bow.objects.all())
	
	
	class Meta:
		model = Card
		fields = ['toemail', 'fromemail', 'message', 'typeface', 'picture', 'bow']