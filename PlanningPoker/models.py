from __future__ import unicode_literals

import datetime
from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(null=True, default=datetime.datetime.now)
    user = models.ForeignKey(User, related_name='owner', blank=True)
    players = models.ManyToManyField(User, related_name='players', blank=True)
    playersFinished = models.ManyToManyField(User, related_name='playersFinished', blank=True)

    def __str__(self):
        return self.name


class Ustory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    score = models.IntegerField()
    game = models.ForeignKey(Game, related_name='game', default='')

    def __str__(self):
        return self.name

class Value(models.Model):
    user = models.ForeignKey(User, related_name='user')
    ustory = models.ForeignKey(Ustory, related_name='ustory')
    value = models.IntegerField()

    def __str__(self):
        return self.name
