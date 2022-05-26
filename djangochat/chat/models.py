from django.db import models
from datetime import datetime


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=32)
    date_created = models.DateTimeField(default=datetime.now, blank=True)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    user = models.CharField(max_length=32)
    room = models.CharField(max_length=32)
    date = models.DateTimeField(default=datetime.now, blank=True)
