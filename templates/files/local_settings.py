import os
from project.settings import *

gettext = lambda s: s
_ = gettext

COMPRESS_ENABLED = True
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*',]

SITE_URL = 'http://localhost:8000/'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '{{ django_secret_key }}'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data.sqlite3'),
    },
}

DGSAUTH_API_KEY = "{{ discogs_api_key }}"
DGSAUTH_API_SECRET = "{{ discogs_api_secret }}"
DGSAUTH_API_ACCESS_TOKEN = "{{ discogs_api_access_token }}"
DGSAUTH_API_ACCESS_SECRET = "{{ discogs_api_access_secret }}"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'dgsproxy'
    }
}

# Discogs proxy settings
DGSPROXY_CACHE_DURATION = 600
