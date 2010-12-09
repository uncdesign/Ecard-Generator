from django.db import models

class Card(models.Model):
	toemail = models.CharField(max_length = 255)
	fromemail = models.CharField(max_length = 255)
	fromname = models.CharField(max_length = 255)
	message = models.TextField()
	sent = models.BooleanField() # Has the email been sent yet
	spam = models.BooleanField() # Is this email spam?
	timestamp = models.DateTimeField(auto_now=True)
	picture = models.ForeignKey('Picture')
	hashid = models.CharField(max_length = 255) # Access via impossible to memorize or guess URL
	ipaddress = models.CharField(max_length = 255) # Who sent this?
	
	def __unicode__(self):
		return u'%s' % (self.id)
	
class Picture(models.Model):
	title = models.CharField(max_length = 255)
	full = models.FileField(upload_to='pictures')
	thumb = models.FileField(upload_to='pictures/thumbs')
	
	class Meta:
		ordering = ['title']
	
	def __unicode__(self):
		return self.title
