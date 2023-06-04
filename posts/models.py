from pyexpat import model
from turtle import mode
from django.db import models


class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
