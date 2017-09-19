from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import EmailMessage
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('The given email must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
        db_index=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    first_time_vote = models.BooleanField(default=True)
    last_time_vote = models.DateTimeField(auto_now_add=True)
    # already_voted_for = ArrayField(
    #     models.CharField(max_length=3, blank=True),
    #     null=True,
    #     blank=True,
    # )
    nric = models.CharField(max_length=12, blank=True)
    mobile = models.CharField(max_length=12, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def has_voted_recently(self):
        x = timezone.localtime(timezone.now()).replace(hour=0, minute=0, second=1, microsecond=1)
        return self.last_time_vote >= x
        # return self.last_time_vote >= timezone.now() - datetime.timedelta(hours=12)

    def __unicode__(self):
        return unicode(self.email)

    def get_full_name(self):
        return self.first_name + self.last_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def email_user(self, subject, message, from_email=None):
        if from_email is None:
            email = settings.DEFAULT_FROM_EMAIL
        else:
            email = from_email
        msg = EmailMessage(subject,
                           message,
                           email,
                           [self.email])

        msg.content_subtype = "html"
        msg.send()

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def username(self):
        return self.email

    @property
    def get_short_name(self):
        return self.email

    class Meta:
        ordering = ['email']


# class FacebookUser(models.Model):
#     user = models.OneToOneField(User)
#
#     facebook_uid = models.PositiveIntegerField(blank=True, null=True)
#     facebook_access_token = models.CharField(blank=True, max_length=255)
#     facebook_access_token_expires = models.PositiveIntegerField(blank=True, null=True)

class SocialMediaUser(models.Model):
    username = models.CharField(max_length=400)
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
        db_index=True,
    )
    first_name = models.CharField(max_length=400, verbose_name='first name')
    last_name = models.CharField(max_length=400, verbose_name='last name')
    UID = models.PositiveIntegerField(blank=True, null=True)
