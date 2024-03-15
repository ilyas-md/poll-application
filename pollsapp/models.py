from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=300)

    def _str_(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def _str_(self):
        return self.option