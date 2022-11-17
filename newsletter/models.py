from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from embed_video.fields import EmbedVideoField

# Create your models here.


class Issue(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Element(models.Model):
    issue = models.ForeignKey(Issue, related_name='elements', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    link_name = models.CharField(max_length=200, null=True, blank=True)
    link_url = models.CharField(max_length=200, null=True, blank=True)


class Episode(models.Model):
    title = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title


class Video(models.Model):
    episode = models.ForeignKey(Episode, related_name='videos', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = [ '-added' ]
