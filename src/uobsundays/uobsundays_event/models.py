from django.db import models
from uobsundays_helpers.helpers import upload_file_path


class EventImageAbstract(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_file_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return self.name

    def total_votes(self):
        return EventVote.objects.filter(event=self.pk).count()

    class Meta:
        ordering = ['name']
        abstract = True


class EventImage(EventImageAbstract):
    class Meta:
        verbose_name = 'June Photo Gallery'
        verbose_name_plural = 'June Photo Galleries'
    pass


class EventImage2(EventImageAbstract):
    class Meta:
        verbose_name = 'July Photo Gallery'
        verbose_name_plural = 'July Photo Galleries'
    pass


class EventImage3(EventImageAbstract):
    class Meta:
        verbose_name = 'November Photo Gallery'
        verbose_name_plural = 'November Photo Galleries'
    pass


class EventVote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    event = models.ForeignKey('uobsundays_event.EventImage', related_name='votes')
    user = models.ForeignKey('uobsundays_user.User', related_name='votes')