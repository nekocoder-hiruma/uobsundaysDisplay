from base import *

DEBUG = TEMPLATE_DEBUG = False

HOSTNAME = 'http://staging.uobsundays.com'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            ':11211'
        ]
    }
}
MIDDLEWARE_CLASSES += (
    'lockdown.middleware.LockdownMiddleware',
)
DATABASES['default']['NAME'] = get_env_setting(
    'DB_NAME',
    'uobsundays_staging'
)

DATABASES['default']['USER'] = get_env_setting(
    'DB_USER',
    'uobsundays_staging'
)

DATABASES['default']['HOST'] = get_env_setting(
    'DB_HOST',
    'postgresql.uobsundays.com'
)

RAVEN_CONFIG['site'] = 'staging'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
AWS_STORAGE_BUCKET_NAME = 'uobsundays-staging'
AWS_ACCESS_KEY_ID = 'AKIAICPMBD54MY5IKOZQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_QUERYSTRING_AUTH = False


# PASSWORD FOR SITE
LOCKDOWN_PASSWORDS = ('evelyn&dann%%')
LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'
LOCKDOWN_ENABLED = 'False'


# OAuth keys
SOCIAL_AUTH_FACEBOOK_KEY = '1452069601765033'
SOCIAL_AUTH_FACEBOOK_SECRET = '0e4774047abef31dbc21c97801a85d55'
