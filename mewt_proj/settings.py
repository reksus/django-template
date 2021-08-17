# external packages
from decouple import config
import django_heroku

# python packages
from pathlib import Path
from datetime import timedelta


BASE_DIR = Path(__file__).resolve().parent.parent

# environment variables
SECRET_KEY = config('SECRET_KEY', '')
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = [config('ALLOWED_HOST')]


INSTALLED_APPS = [

	# the following whitenoise app may be uncommented if you want to utilize whitenoise for development as well
	# in that case you need to separately run 'python manage.py collecstatic' before runserver
	# for further info refer 'http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development'

	# 'whitenoise.runserver_nostatic',

	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'rest_framework',
	'rest_framework_simplejwt',

	# # following app can be included if the project requires background tasks
	# # this app is to be installed before any of the custom apps:
	'django_dramatiq',

	# follwing sample app may be removed in the real project if so required
	'sample_app',

	# other apps can be added after this
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware', # <-- new addition
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mewt_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mewt_proj.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER', default=''),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default=''),
        'PORT': config('DB_PORT', default=''),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Activate Django-Heroku.
django_heroku.settings(locals())


# # SETUP JWT AUTHENTICATION
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
#     'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
# }

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
# }



# # SETUP RABBITMQ TASK QUEUE
# DRAMATIQ_BROKER = {
#     "BROKER": "dramatiq.brokers.rabbitmq.RabbitmqBroker",
#     "OPTIONS": {
#         "url": config('CLOUDAMQP_URL'),
#     },
#     "MIDDLEWARE": [
#         "dramatiq.middleware.Prometheus",
#         "dramatiq.middleware.AgeLimit",
#         "dramatiq.middleware.TimeLimit",
#         "dramatiq.middleware.Callbacks",
#         "dramatiq.middleware.Retries",
#         "django_dramatiq.middleware.DbConnectionsMiddleware",
#         "django_dramatiq.middleware.AdminMiddleware",
#     ]
# }
