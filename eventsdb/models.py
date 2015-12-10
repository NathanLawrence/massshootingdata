from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Location(models.Model):
	city = models.CharField(max_length = 100)
	state = models.CharField(max_length = 2)

class Shooter(models.Model):
	name = models.Charfield(max_length = 150)
	description = models.TextField(null = True)
	event = models.ForeignKey(Event)

class Article(models.Model):
	headline  = models.CharField(max_length  = 200)
	publisher = models.CharField(max_length = 50)
	event = models.ForeignKey(Event)
	url = models.URLField()

class Event(models.Model):
	slug = models.SlugField()
	location = models.ForeignKey(Location)
	date = models.DatetimeField('shooting date')
	dead = models.IntegerField()
	injured = models.IntegerField()

class Weapon(models.Model):
	name = models.CharField(max_length = 150)
	description = models.TextField(null = True)

class WeaponEvent(models.Model):
	event = models.ForeignKey(Event)
	weapon = models.ForeignKey(Weapon)