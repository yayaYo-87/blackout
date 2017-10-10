from config.settings import *
DEBUG = False
ALLOWED_HOSTS = ['www.testblackout.pythonanywhere.com', 'testblackout.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blackout',
        'PASSWORD': 'user1111',
        'HOST': 'localhost',
        'USER': 'super',
        'PORT': '10551'
    }
}

ADMINS = [
    ('Blackout', 'zubkov@smoothie.digital')
]

SITE_HOST = 'testblackout.pythonanywhere.com'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

SERVER_EMAIL = EMAIL_HOST_USER

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'