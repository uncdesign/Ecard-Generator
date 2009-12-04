from django.db import models
from django.forms import ModelForm, ModelChoiceField, EmailField, CharField
from django.forms.widgets import RadioSelect, Textarea
from generator.models import Card, Picture, Border, Typeface
from django.utils.safestring import mark_safe


class PictureModelChoiceField(ModelChoiceField):
	def label_from_instance(self,obj):
		return mark_safe('<img src="%s" rel="%s">' % (obj.thumb.url,obj.full.url))

class BorderModelChoiceField(ModelChoiceField):
	def label_from_instance(self,obj):
		return mark_safe('<img src="%s" rel="%s">' % (obj.thumb.url,obj.preview.url))

class TypefaceModelChoiceField(ModelChoiceField):
	def label_from_instance(self,obj):
		return mark_safe('<span style="font-family:%s">%s</span>' % (obj.fontstack,obj.title))

class CreateCardForm(ModelForm):
	toemail = EmailField(required=True, max_length=255)
	fromemail = EmailField(required=True, max_length=255)
	picture = PictureModelChoiceField(widget=RadioSelect, queryset=Picture.objects.all(), required=True, empty_label=None)
	typeface = TypefaceModelChoiceField(widget=RadioSelect, queryset=Typeface.objects.all(), required=True, empty_label=None, initial='2')
	border = BorderModelChoiceField(widget=RadioSelect, queryset=Border.objects.all(), required=True, empty_label=None, initial='1')
	message = CharField(widget=Textarea, required=True, max_length=230)
	
	class Meta:
		model = Card
		fields = ['picture', 'border', 'message', 'typeface', 'toemail', 'fromemail', 'fromname']
		
		