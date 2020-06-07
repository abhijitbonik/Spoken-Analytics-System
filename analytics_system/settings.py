"""
Django settings for analytics_system project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from .config import *
from celery.schedules import crontab

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k2uuq8w9$%epynk6jyzqv^&zn%c%q&-e!93tgfsth7_73a*dia'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djgeojson',
    'leaflet',
    'mathfilters',
    'dashboard',
    'corsheaders',
    'logs_api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'analytics_system.urls'

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

WSGI_APPLICATION = 'analytics_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # Default database
    'default': {
        'ENGINE': 'djongo',
        'NAME': MongoDB,
    },
    # Database used for authentication
    'spoken': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': '',                            # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',
    },
}

DATABASE_ROUTERS = [
    # Router to use 'spoken' database for authentications
    'dashboard.router.AuthRouter',
]

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i0n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I0N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CORS_ORIGIN_ALLOW_ALL = True

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
CELERY_IMPORTS = (
    'dashboard.calculation_scripts.averageStats',
    'dashboard.calculation_scripts.cameFromActivityStats',
    'dashboard.calculation_scripts.cameFromStats',
    'dashboard.calculation_scripts.dailyStats',
    'dashboard.calculation_scripts.eventStats',
    'dashboard.calculation_scripts.exitLinkStats',
    'dashboard.calculation_scripts.fossStats',
    'dashboard.calculation_scripts.locationStats',
    'dashboard.calculation_scripts.monthlyStats',
    'dashboard.calculation_scripts.pageViewActivityStats',
    'dashboard.calculation_scripts.sourcesStats',
    'dashboard.calculation_scripts.systemStats',
    'dashboard.calculation_scripts.visitorActivityStats',
    'dashboard.calculation_scripts.visitorInfoStats',
    'dashboard.calculation_scripts.visitorPathStats',
    'dashboard.calculation_scripts.visitorSpotStats',
    'dashboard.calculation_scripts.weeklyStats',
    'dashboard.calculation_scripts.yearlyStats',
)

# Other Celery settings
CELERY_BEAT_SCHEDULE = {
    'average_statistics': {
        'task': 'dashboard.calculation_scripts.averageStats.average_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'came_from_activity_statistics': {
        'task': 'dashboard.calculation_scripts.cameFromActivityStats.came_from_activity_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'came_from_statistics': {
        'task': 'dashboard.calculation_scripts.cameFromStats.came_from_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'daily_statistics': {
        'task': 'dashboard.calculation_scripts.dailyStats.daily_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'event_statistics': {
        'task': 'dashboard.calculation_scripts.eventStats.event_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'exit_link_statistics': {
        'task': 'dashboard.calculation_scripts.exitLinkStats.exit_link_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'foss_statistics': {
        'task': 'dashboard.calculation_scripts.fossStats.foss_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'location_statistics': {
        'task': 'dashboard.calculation_scripts.locationStats.location_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'monthly_statistics': {
        'task': 'dashboard.calculation_scripts.monthlyStats.monthly_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'page_view_activity_statistics': {
        'task': 'dashboard.calculation_scripts.pageViewActivityStats.page_view_activity_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'sources_statistics': {
        'task': 'dashboard.calculation_scripts.sourcesStats.sources_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'system_statistics': {
        'task': 'dashboard.calculation_scripts.systemStats.system_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'visitor_activity_statistics': {
        'task': 'dashboard.calculation_scripts.visitorActivityStats.visitor_activity_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'visitor_info_statistics': {
        'task': 'dashboard.calculation_scripts.visitorInfoStats.visitor_info_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'visitor_path_statistics': {
        'task': 'dashboard.calculation_scripts.visitorPathStats.visitor_path_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'visitor_spot_statistics': {
        'task': 'dashboard.calculation_scripts.visitorSpotStats.visitor_spot_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'weekly_statistics': {
        'task': 'dashboard.calculation_scripts.weeklyStats.weekly_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
    'yearly_statistics': {
        'task': 'dashboard.calculation_scripts.yearlyStats.yearly_statistics',
        'schedule': crontab(minute=0, hour=0),  # execute daily at midnight
    },
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GEOIP_PATH  = BASE_DIR + '/geodb/'

MONITOR_QUEUE_ITERATION_DELAY = 5  # delay between successive iterations of monitor_queue.py, in seconds

USE_MIDDLEWARE_LOGS = True  # whether to use middleware logs or client-side JS logs system

SAVE_LOGS_WITH_CELERY = False

MONGO_BULK_INSERT_COUNT = 5  # change to a large value like 10000 later

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (20.5937, 78.9629),
    'DEFAULT_ZOOM': 4,
}
