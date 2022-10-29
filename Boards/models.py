from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BoardData(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TopicData(models.Model):
    title = models.CharField(max_length=150)
    board = models.ForeignKey(BoardData, related_name='topic', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='topic', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostData(models.Model):
    content = models.CharField(max_length=250)
    topic = models.ForeignKey(TopicData, related_name='post', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
