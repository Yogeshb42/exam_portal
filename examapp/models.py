from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^[789]\d{9}$', message="Numeric Field. Only 10 digits allowed.")

subject_choice =(
    ("Maths", "Maths"),
    ("Science", "Science"),
)

class CustomUser(AbstractUser):
    phone_number = models.CharField(validators=[phone_regex], max_length=10, unique=True)
    subject = models.CharField(max_length=255, blank=True, null=True, choices=subject_choice)

    def __str__(self):
        return self.username

class ExamModel(models.Model):
    subject = models.CharField(max_length=200,choices = subject_choice)
    question_name = models.CharField(max_length=200,null=True)
    option1 = models.CharField(max_length=200,null=True)
    option2 = models.CharField(max_length=200,null=True)
    option3 = models.CharField(max_length=200,null=True)
    option4 = models.CharField(max_length=200,null=True)
    answer = models.CharField(max_length=200,null=True)
    
    # def __str__(self):
    #     return self.question

class Result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, blank=True)
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    wrong_answers = models.IntegerField(default=0)
    skipped_questions = models.IntegerField(default=0)
    subject = models.CharField(max_length=200, blank=True, null=True)

    # def __str__(self):
    #     return str(self.score)