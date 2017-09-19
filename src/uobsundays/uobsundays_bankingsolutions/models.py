from django.db import models
from ckeditor.fields import RichTextField
from uobsundays_helpers.helpers import upload_file_path


class BankingSolutionsImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_file_path, blank=True, null=True)
    description = models.CharField(max_length=200)
    additional_content = RichTextField(blank=True, null=True)
    link = models.CharField(max_length=200)
    color = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
