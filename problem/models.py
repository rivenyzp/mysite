from django.db import models
from user.models import my_User
from django.contrib.auth.models import User
# Create your models here.

class problem(models.Model):
    problem_name = models.CharField(max_length=20)
    problem_describe = models.TextField()
    problem_date = models.DateField()
    problem_answer = models.CharField(max_length=50)
    problem_author = models.ForeignKey(my_User)

    def __str__(self):
        return  self.problem_name
