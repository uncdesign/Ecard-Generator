from django.db import models

class Card(models.Model):
	toemail = models.CharField(max_length = 255)
	fromemail = models.CharField(max_length = 255)
	message = models.TextField()
	sent = models.BooleanField()
	picture = models.ForeignKey('Picture')
	bow = models.ForeignKey('Bow')
	typeface = models.ForeignKey('Typeface')
	
class Picture(models.Model):
	title = models.CharField(max_length = 255)
	full = models.FileField(upload_to='pictures')
	thumb = models.FileField(upload_to='pictures/thumbs')

class Bow(models.Model):
	title = models.CharField(max_length = 255)
	full = models.FileField(upload_to='bows')
	thumb = models.FileField(upload_to='bows/thumbs')	

class Typeface(models.Model):
	title = models.CharField(max_length = 255)
	fontstack = models.TextField()

