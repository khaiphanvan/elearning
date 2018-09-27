from .base import *

DEBUG = False
ADMINS = (
    ('Khai Phan', 'email@mydomain.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'khaiphan',
        'PASSWORD': '123456',
    }
}
