from base import *

DEBUG = TEMPLATE_DEBUG = True

HOSTNAME = 'http://dev.uobsundays.com:8000'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
AWS_STORAGE_BUCKET_NAME = 'uobsundays-development'
AWS_ACCESS_KEY_ID = 'AKIAJYSCHDRDVAUDLRYA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_QUERYSTRING_AUTH = False


# OAuth keys
SOCIAL_AUTH_FACEBOOK_KEY = '105058613179408'
SOCIAL_AUTH_FACEBOOK_SECRET = '1ebbd2f9160cbfcf5e69bad3ca3d18c3'
