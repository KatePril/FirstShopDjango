from django.db import models

# Create your models here.
class Question(models.Model):
    number = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField()

class Network(models.Model):
    name = models.TextField