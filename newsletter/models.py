from django.db import models

# Create your models here.


class Issue(models.Model):
    title = models.CharField(max_length=200, null=True)

    first_impressions_robert_title = models.CharField(max_length=200, null=True)
    first_impressions_robert_desc = models.CharField(max_length=200, null=True)
    first_impressions_robert_body = models.TextField(blank=True)

    first_impressions_stephen_title = models.CharField(max_length=200, null=True)
    first_impressions_stephen_desc = models.CharField(max_length=200, null=True)
    first_impressions_stephen_body = models.TextField(blank=True)

    first_impressions_michael_title = models.CharField(max_length=200, null=True)
    first_impressions_michael_desc = models.CharField(max_length=200, null=True)
    first_impressions_michael_body = models.TextField(blank=True)

    never_gets_old_title = models.CharField(max_length=200, null=True)
    never_gets_old_desc = models.CharField(max_length=200, null=True)
    never_gets_old_body = models.TextField(blank=True)

    composer_spotlight_title = models.CharField(max_length=200, null=True)
    composer_spotlight_desc = models.CharField(max_length=200, null=True)
    composer_spotlight_body = models.TextField(blank=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title


class Episode(models.Model):
    title = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title
