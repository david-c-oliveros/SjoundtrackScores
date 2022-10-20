from django.db import models

# Create your models here.


class Summary(models.Model):
    intro = models.TextField(blank=True)
    body = models.TextField(blank=True)


class FirstImpressions(models.Model):
    first_title = models.CharField(max_length=200, null=True)
    first_desc = models.CharField(max_length=200, null=True)
    first_body = models.TextField(blank=True)

    second_title = models.CharField(max_length=200, null=True)
    second_desc = models.CharField(max_length=200, null=True)
    second_body = models.TextField(blank=True)

    third_title = models.CharField(max_length=200, null=True)
    third_desc = models.CharField(max_length=200, null=True)
    third_body = models.TextField(blank=True)


class NeverGetsOld(models.Model):
    title = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=200, null=True)
    body = models.TextField(blank=True)


class ComposerSpotlight(models.Model):
    title = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=200, null=True)
    body = models.TextField(blank=True)


class Episode(models.Model):
    title = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title


class Issue(models.Model):
    title = models.CharField(max_length=200, null=True)

    summary = models.ForeignKey(Summary, null=True, on_delete=models.SET_NULL)
    first_impressions = models.ForeignKey(FirstImpressions, null=True, on_delete=models.SET_NULL)
    never_gets_old = models.ForeignKey(NeverGetsOld, null=True, on_delete=models.SET_NULL)
    composer_spotlight = models.ForeignKey(ComposerSpotlight, null=True, on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title
