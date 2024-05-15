from django.db import models

# Create your models here.
class Question(models.Model):
  question_text = models.CharField(max_length=255, default="Placeholder")
  date = models.DateTimeField()

  def __str__(self):
    return f"Id: {self.id} | {self.question_text}"  # O la representación que desees


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField()

    def __str__(self):
      return f"Id: {self.id} | {self.answer_text}"  # O la representación que desees

    def is_trending(self):
        return self.likes >= 3