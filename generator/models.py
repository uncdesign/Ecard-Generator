from django.db import models

class Card(models.Model):
	toemail = models.CharField(max_length = 255)
	fromemail = models.CharField(max_length = 255)
	fromname = models.CharField(max_length = 255)
	message = models.TextField()
	sent = models.BooleanField() # Has the email been sent yet
	timestamp = models.DateTimeField(auto_now=True)
	picture = models.ForeignKey('Picture')
	border = models.ForeignKey('Border', blank=True)
	typeface = models.ForeignKey('Typeface')
	hashid = models.CharField(max_length = 255) # Access via impossible to memorize or guess URL
	
	def __unicode__(self):
		return u'%s' % (self.id)
	
class Picture(models.Model):
	title = models.CharField(max_length = 255)
	full = models.FileField(upload_to='pictures')
	thumb = models.FileField(upload_to='pictures/thumbs')
	bordercolor = models.CharField(max_length = 255, blank=True)
	
	def __unicode__(self):
		return self.title

class Border(models.Model):
	title = models.CharField(max_length = 255)
	cell_1 = models.FileField(upload_to='borders') # Starting at the top left, moving clockwise around a square
	cell_2 = models.FileField(upload_to='borders', blank=True)
	cell_3 = models.FileField(upload_to='borders', blank=True)
	cell_4 = models.FileField(upload_to='borders', blank=True)
	cell_5 = models.FileField(upload_to='borders', blank=True)
	cell_6 = models.FileField(upload_to='borders', blank=True)
	cell_7 = models.FileField(upload_to='borders', blank=True)
	cell_8 = models.FileField(upload_to='borders', blank=True)
	thumb = models.FileField(upload_to='borders/thumbs')
	bgcolor = models.CharField(max_length = 255, blank=True)	# In case border color bleeds into main text area

	def __unicode__(self):
		return self.title

class Typeface(models.Model):
	title = models.CharField(max_length = 255)
	fontstack = models.TextField() # CSS font stack

	def __unicode__(self):
		return self.title
