from django.db import models

class Ecard(models.Model):
	to = models.CharField(max_length = 256)

# Create your models here.
