from django.db import models
from django.http import JsonResponse

# Create your models here.
class SentimentModel(models.Model):

    comment = models.CharField(max_length=500,default='some string')


def __str__(self):
        return self.comment

