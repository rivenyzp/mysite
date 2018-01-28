from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class my_User(User):
    solve_sum = models.IntegerField(default=0)
    solve_Web = models.IntegerField(default=0)
    solve_Reverse = models.IntegerField(default=0)
    solve_Pwn = models.IntegerField(default=0)


    def __str__(self):
        return  self.username


