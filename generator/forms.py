from django.db import models
from django.forms import ModelForm, ModelChoiceField, EmailField, CharField
from django.forms.widgets import RadioSelect, Textarea
from generator.models import Card, Picture
from django.utils.safestring import mark_safe


class PictureModelChoiceField(ModelChoiceField):
	def label_from_instance(self,obj):
		return mark_safe('<img src="%s" rel="%s">' % (obj.thumb.url,obj.full.url))

class CreateCardForm(ModelForm):
	toemail = EmailField(required=True, max_length=255)
	fromemail = EmailField(required=True, max_length=255)
	picture = PictureModelChoiceField(widget=RadioSelect, queryset=Picture.objects.all(), required=True, empty_label=None)
	message = CharField(widget=Textarea, required=True, max_length=230)
	
	class Meta:
		model = Card
		fields = ['picture', 'message', 'toemail', 'fromemail', 'fromname']
		
		