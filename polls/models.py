from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


# Here we are creating two models one is for Questions  and another for Choices
# each Question contains a text and pub_date and Choices contains a text and number of votes
# Each choice is  related  to a single question
class  Question(models.Model):
    question_text = models.CharField(max_length =20)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() -datetime.timedelta(days =1 )

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    choice_text = models.CharField(max_length =8)
    votes = models.IntegerField(default =0 )

    def __str__(self):
        return self.choice_text
