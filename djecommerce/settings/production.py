from .base import *
import django_heroku
DEBUG = True
ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "d3ivduek0cvv3s",
        'USER': "eertwpddbufqos",
        'PASSWORD': "d2ece9002294357e2548b8cf1f266198e70f54835815a885c6f7754a59935a81",
        'HOST': "ec2-23-21-87-183.compute-1.amazonaws.com",
        'PORT': '5432'
    }
}


STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')

django_heroku.settings(locals())
