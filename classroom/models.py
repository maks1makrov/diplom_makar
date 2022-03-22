from django.contrib.auth.models import User
from django.db import models


class Materials(models.Model):
    name = models.CharField(max_length=100, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.name

class KonspectOne(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ideologia = models.CharField(max_length=150)
    link = models.URLField()
    since = models.CharField(max_length=150)
    polit_ideologia = models.CharField(max_length=150)


class QuestionForKonspect(models.Model):
    material = models.ForeignKey(Materials, on_delete=models.PROTECT, verbose_name='тема', related_name="questions")
    text = models.TextField(verbose_name="вопрос")

    def __str__(self):
        return f'question for {self.material}'


class AnswerForKonspect(models.Model):
    question = models.ForeignKey(QuestionForKonspect, on_delete=models.PROTECT)
    answer = models.TextField(verbose_name='ответ')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'answer for {self.question.text} - for {self.user.username}'