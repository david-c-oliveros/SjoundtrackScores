from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.


class Issue(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Element(models.Model):
    issue = models.ForeignKey(Issue, related_name='elements', null=True, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    image = models.ImageField(null=True, blank=True)


class Episode(models.Model):
    title = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title
