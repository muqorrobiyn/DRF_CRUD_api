from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

# Create your models here.
