from django.db.models.deletion import CASCADE
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateField('date published')

    def __str__(self) -> str:
        return self.question_text   


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
