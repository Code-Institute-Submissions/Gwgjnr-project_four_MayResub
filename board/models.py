from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_posts"
    )
    summary = models.TextField(blank=True)
    location = models.TextField()
    requirements = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    event_start = models.DateTimeField()
    spots = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=1)
    signed_up = models.ManyToManyField(
        User, related_name='event_numbers', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.titles
