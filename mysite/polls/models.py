import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question (models.Model):
  Question_text = models.CharField(max_length=200)
  publish_data= models.DateTimeField("date published")


  def __str__(self):
        return self.Question_text

  def was_recently_published(self):
      now = timezone.now()
      return now - datetime.timedelta(days=1) <= self.publish_data <= now
  @property
  def total_votes(self):
        return sum(choice.votes for choice in self.choice_set.all())

class Choice (models.Model):
  question = models.ForeignKey(Question,on_delete=models.CASCADE)
   # When the related Question is deleted, delete this Choice too.
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
        return self.choice_text

  def percentage_of_votes(self):
        if self.question.total_votes > 0:
            return (self.votes / self.question.total_votes) * 100
        else:
            return 0
