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


class Question(models.Model):
    material = models.ForeignKey(Materials, on_delete=models.PROTECT, verbose_name='тема')
    text = models.TextField(verbose_name="вопрос")


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.TextField(verbose_name='ответ')
    user = models.ForeignKey(User, on_delete=models.PROTECT)