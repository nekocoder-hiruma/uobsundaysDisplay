from django.db import models
from ckeditor.fields import RichTextField
from uobsundays_helpers.helpers import upload_file_path
from uobsundays_youngartist.constants import LOCATION_CHOICES, PRIZE_CHOICES, CATEGORY_CHOICES


class YoungArtistOverview(models.Model):
    header = models.CharField(max_length=200)
    content = RichTextField()
    Contest_Detail_Place = RichTextField()
    Contest_Detail_Date = RichTextField()
    Contest_Detail_Session = RichTextField()
    Sign_Up = RichTextField()
    Vote = RichTextField()
    # Judging = RichTextField()
    Winner_Prize = RichTextField()


class YoungArtistSubmission(models.Model):
    image = models.ImageField(upload_to=upload_file_path, blank=True, null=True)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)
    location = models.CharField(max_length=3, choices=LOCATION_CHOICES)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.artist

    class Meta:
        ordering = ['created']

# class YoungArtistShortlisted(models.Model):
#     image = models.ImageField(upload_to=upload_file_path, blank=True, null=True)
#     title = models.CharField(max_length=200)
#     artist = models.CharField(max_length=200)
#     age = models.CharField(max_length=200)
#     created = models.DateTimeField(auto_now_add=True, db_index=True)
#     modified = models.DateTimeField(auto_now=True, db_index=True)
#     location = models.CharField(max_length=3, choices=LOCATION_CHOICES)
#     likes = models.IntegerField(default=0)
#
#     def __unicode__(self):
#         return self.artist


class YoungArtistWinner(models.Model):
    prize = models.CharField(max_length=20, choices=PRIZE_CHOICES)
    artist_photo = models.ImageField(upload_to=upload_file_path, blank=True, null=True)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    artist_age = models.CharField(max_length=200)
    number_of_likes = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __unicode__(self):
        return self.artist