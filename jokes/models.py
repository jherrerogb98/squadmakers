from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Joke(models.Model):

    class Choices(models.TextChoices):
        CHUCK = 'chuck', "chuck"
        DAD = 'dad', 'dad'

    text = models.TextField(max_length = 1000)
    type = models.CharField(max_length=30, choices = Choices.choices, default = 1)
    created = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.text
