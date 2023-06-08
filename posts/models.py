from pyexpat import model
from turtle import mode
from django.db import models


class Hashtag(models.Model):
    title = models.CharField(max_length=36)


class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField(Hashtag)

    @property
    def hashtags_list(self):
        return self.hashtags.all()
