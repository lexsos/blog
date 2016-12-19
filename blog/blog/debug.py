from .common import *


DEBUG = True

SECRET_KEY = 'rt$2t!lnn%&*$vf4^!&ypd=(tt+u5mu072-voxt@b@1t)2@kwb'

ALLOWED_HOSTS = ['127.0.0.1', ]
INTERNAL_IPS = ['127.0.0.1', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]