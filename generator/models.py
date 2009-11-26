from django.db import models
from base64 import urlsafe_b64encode, urlsafe_b64decode

class Card(models.Model):
	toemail = models.CharField(max_length = 255)
	fromemail = models.CharField(max_length = 255)
	message = models.TextField()
	sent = models.BooleanField()
	timestamp = models.DateField(auto_now=True)
	picture = models.ForeignKey('Picture')
	bow = models.ForeignKey('Bow')
	typeface = models.ForeignKey('Typeface')
	
	def __unicode__(self):
		return u'%s / last-modified: %s / hash: %s' % (self.id, self.timestamp, urlsafe_b64encode(str(self.id)))
	
class Picture(models.Model):
	title = models.CharField(max_length = 255)
	full = models.FileField(upload_to='pictures')
	thumb = models.FileField(upload_to='pictures/thumbs')
	
	def __unicode__(self):
		return self.title

class Bow(models.Model):
	title = models.CharField(max_length = 255)
	full = models.FileField(upload_to='bows')
	thumb = models.FileField(upload_to='bows/thumbs')	

	def __unicode__(self):
		return self.title

class Typeface(models.Model):
	title = models.CharField(max_length = 255)
	fontstack = models.TextField()

	def __unicode__(self):
		return self.title
