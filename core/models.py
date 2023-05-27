from django.db import models

# Create your models here.
class Question(models.Model):
    number = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField()
    
    def __str__(self):
        return f'{self.question}'

class Network(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'