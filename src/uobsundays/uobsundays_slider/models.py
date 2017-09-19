from django.db import models
from uobsundays_helpers.helpers import upload_file_path

# Create your models here.
class Slide(models.Model):
    name = models.CharField(max_length=100)
    slide = models.ImageField(upload_to=upload_file_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title