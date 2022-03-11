from django.db import models


class Materials(models.Model):
    name = models.CharField(max_length=100, unique=True)
    text = models.TextField()

