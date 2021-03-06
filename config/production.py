from config.settings import *
DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blackout',
        'PASSWORD': '1111',
        'HOST': 'localhost',
        'USER': 'postgres',
    }
}

ADMINS = [
    ('Blackout', 'zubkov@smoothie.digital')
]

# SITE_HOST = 'testblackout.pythonanywhere.com'
SITE_HOST = '188.225.11.16'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

SERVER_EMAIL = EMAIL_HOST_USER

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'