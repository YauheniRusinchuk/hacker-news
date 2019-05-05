from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title       = models.CharField(max_length=300, blank=False)
    text        = models.TextField(blank=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    like        = models.ManyToManyField(User, related_name='count_like')

    class Meta:
        ordering = ['-create_time']


    def get_absolute_url(self):
        return reverse('home:detail_page', kwargs={'pk': self.pk})


    def __str__(self):
        return f"{self.title}"
