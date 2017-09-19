"""
Django settings for UOBSundays.
For more information on this file, see
https://docs.djangoproject_name.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject_name.com/en/1.8/ref/settings/
"""

# Build paths inside the project_name like this: os.path.join(BASE_DIR, ...)
import os
from os.path import dirname, abspath, basename, join, normpath
from django.core.exceptions import ImproperlyConfigured
import sys


def get_env_setting(setting, default=None):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        if default is None:
            error_msg = "Set the %s env variable" % setting
            raise ImproperlyConfigured(error_msg)
        else:
            return default


SITE_ROOT = dirname(dirname(dirname(abspath(__file__))))
SITE_NAME = basename(SITE_ROOT)
sys.path.append(SITE_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings.local")

ADMINS = (('Wai Keat', 'waikeat@kamiworks.com'),)
MANAGERS = ADMINS

FROM_EMAIL = 'hello@uobsundays.com'
DEFAULT_FROM_EMAIL = 'hello@uobsundays.com'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject_name.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!&@xp&sgo^n6wo%a0478fbdomdlo5-n9j4j^5)b*axxcitk2!x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.uobsundays.com', 'django-dbbackup']

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'storages',
    'raven.contrib.django.raven_compat',
    'djrill',
    'dbbackup',
    'djangosecure',
    'ckeditor',
    'lockdown',
    'social.apps.django_app.default',
    'imagefit',
)

LOCAL_APPS = (
    'uobsundays_website',
    'uobsundays_event',
    'uobsundays_helpers',
    'uobsundays_slider',
    'uobsundays_user',
    'uobsundays_bankingsolutions',
    'uobsundays_youngartist',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DJANGO_TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

THIRD_PARTY_CONTEXT_PROCESSORS = (
)

LOCAL_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

TEMPLATE_CONTEXT_PROCESSORS = \
    DJANGO_TEMPLATE_CONTEXT_PROCESSORS + THIRD_PARTY_CONTEXT_PROCESSORS + LOCAL_CONTEXT_PROCESSORS

# Database
# https://docs.djangoproject_name.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3' if 'test' in sys.argv else 'django.db.backends.postgresql_psycopg2',
        # NOQA Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': get_env_setting('uobsundays_DB_NAME',
                                'uobsundays'),
        'USER': get_env_setting('uobsundays_DB_USER',
                                'uobsundays'),
        'PASSWORD': get_env_setting('uobsundays_DB_PASSWORD',
                                    'ldsjl_039'),
        'HOST': get_env_setting('uobsundays_DB_HOST',
                                '127.0.0.1'),
        'PORT': get_env_setting('uobsundays_DB_PORT',
                                '5432'),
    }
}

# Internationalization
# https://docs.djangoproject_name.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-sg'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Login/Logout Url
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'
LOGOUT_URL = '/logout/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject_name.com/en/1.7/howto/static-files/

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)

LOCALE_PATHS = (
    normpath(join(SITE_ROOT, 'locale')),
)

# Raven Config
# Logging to www.getsentry.com

if 'test' not in sys.argv:
    RAVEN_CONFIG = {
        'site': 'development',
        'dsn': 'https://bca941d4b1dc43a190cf905884dc14c2:f034a2c13c5047b096f9949da165abc7@app.getsentry.com/45903',
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

# Compressor Settings
COMPRESS_ENABLED = True
if DEBUG:
    COMPRESS_DEBUG_TOGGLE = 'nocompress'
# Since we're serving from several servers
COMPRESS_CSS_HASHING_METHOD = 'content'

# User Model
AUTH_USER_MODEL = 'uobsundays_user.User'

# Djrill Config for Mandrill
MANDRILL_API_KEY = "LeguVqrVxMuoAWNCH-ws9w"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

# MailChimp Config
MAILCHIMP_APIKEY = ''

# DBBackup S3 Config
DBBACKUP_STORAGE = 'dbbackup.storage.s3_storage'
DBBACKUP_S3_BUCKET = ''
DBBACKUP_S3_ACCESS_KEY = ''
DBBACKUP_S3_SECRET_KEY = ''

# CKEditor Config
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"

# Security Config
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_FRAME_DENY = True

# Authentication for Social Media Backends
AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GooglePlusAuth',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Facebook testing
TEST_FACEBOOK_USER = 'lltohlf_laustein_1438744788@tfbnw.net'
TEST_FACEBOOK_PASSWORD = 'cat'

# Extra Facebook settings
SOCIAL_AUTH_FACEBOOK_SCOPE = ['public_profile', 'email']
FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'touch'}
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', # needed starting from protocol v2.4
}
URL_PATH = ''

# Social auth pipeline
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    # 'social.pipeline.social_auth.associate_by_email', # Pipeline that associate each social auth via emails
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

# Social Auth custom settings
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email', 'first_name', 'last_name']
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['email', 'first_name', 'email']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/littleartcontest/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/littleartcontest/vote_error/'
SOCIAL_AUTH_USER_MODELS = 'uobsundays_user.SocialMediaUser'

# Google+ Settings
SOCIAL_AUTH_GOOGLE_PLUS_KEY = '237396743157-7u5k46617udh53ojm3d70vudtp65uda6.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = 'H133Xt5jhmXWI59sqGlsqSh1'
SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = [
    'https://www.googleapis.com/auth/plus.login',
    'https://www.googleapis.com/auth/userinfo.email'
]

# Imagefit settings
IMAGEFIT_ROOT = 'public'
