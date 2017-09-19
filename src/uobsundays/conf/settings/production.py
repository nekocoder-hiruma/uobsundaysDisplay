from base import *

DEBUG = TEMPLATE_DEBUG = False

HOSTNAME = 'http://www.uobsundays.com'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            ':11211'
        ]
    }
}

DATABASES['default']['NAME'] = get_env_setting(
    'DB_NAME',
    'uobsundays_production'
)

DATABASES['default']['USER'] = get_env_setting(
    'DB_USER',
    'uobsundays_production'
)

DATABASES['default']['HOST'] = get_env_setting(
    'DB_HOST',
    'postgresql.uobsundays.com'
)

RAVEN_CONFIG['site'] = 'production'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
AWS_STORAGE_BUCKET_NAME = 'uobsundays-production'
AWS_ACCESS_KEY_ID = 'AKIAJVRCEWTBCYZDMZLQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_QUERYSTRING_AUTH = False

# OAuth keys
SOCIAL_AUTH_FACEBOOK_KEY = '1450074521964541'
SOCIAL_AUTH_FACEBOOK_SECRET = '13bdd683da621421a49f3fa3492c42da'

# Security Settings
SESSION_COOKIE_SECURE = True
