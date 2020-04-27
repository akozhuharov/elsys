from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=25)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
