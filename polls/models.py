import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    def __str__(self):
        return self.question_text

    def was_published_recentry(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recentry.admin_order_field = 'pub_date'
    was_published_recentry.boolean = True
    was_published_recentry.short_description = 'Published recentry?'





class Choice(models.Model):
    question = models.ForeignKey(to=Question, verbose_name=None, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
