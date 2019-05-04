from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title       = models.CharField(max_length=300, blank=False)
    text        = models.TextField(blank=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_time']


    def __str__(self):
        return f"{self.title}"
