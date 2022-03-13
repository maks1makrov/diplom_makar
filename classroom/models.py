from django.contrib.auth.models import User
from django.db import models


class Materials(models.Model):
    name = models.CharField(max_length=100, unique=True)
    text = models.TextField()

class KonspectOne(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ideologia = models.CharField(max_length=150)
    link = models.URLField()
    since = models.CharField(max_length=150)
    polit_ideologia = models.CharField(max_length=150)
