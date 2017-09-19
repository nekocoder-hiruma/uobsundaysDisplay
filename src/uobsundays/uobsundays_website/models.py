from django.db import models
from ckeditor.fields import RichTextField
from uobsundays_helpers.helpers import upload_file_path


class SignupContent(models.Model):
    header = models.CharField(max_length=200)
    content = RichTextField()
    EventDetailVenue = RichTextField()
    EventDetailDate = RichTextField()
    EventDetailSession = RichTextField()


class Branches(models.Model):
    name = models.CharField(max_length=200)
    content = RichTextField()
    map = models.TextField(blank=True, null=True)

    BRANCH_CHOICES = (
        ('O', 'Other'),
        ('M', 'Main'),
    )
    branches = models.CharField(max_length=1, choices=BRANCH_CHOICES)

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    def __unicode__(self):
        return self.name


class HomepageImage(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    fg = models.ImageField(upload_to=upload_file_path, blank=True, null=True)
    bg = models.ImageField(upload_to=upload_file_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['created']

    def firstbg(self):
        return bg.Objects.get(pk=1)

    def __unicode__(self):
        return self.name