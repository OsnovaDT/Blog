"""Settings of the project"""

from os.path import join
from pathlib import Path

from django.urls import reverse_lazy
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'post',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3_2',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

LOGIN_URL = reverse_lazy('accounts:login')

LOGIN_REDIRECT_URL = reverse_lazy('post:all_posts')

LOGOUT_REDIRECT_URL = reverse_lazy('post:all_posts')

### STATIC ###

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    ("", join(BASE_DIR, "static")),
]

IMAGES_RELATIVE_PATH = "/images/"

IMAGES_ROOT = join(BASE_DIR, "static", IMAGES_RELATIVE_PATH)

### MEDIA ###

MEDIA_URL = '/media/'

MEDIA_ROOT = join(BASE_DIR, "media")

### TIME ###

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

### Internationalization ###

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

### OTHER ###

SECRET_KEY = config('SECRET_KEY')

ROOT_URLCONF = 'blog.urls'

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'blog.wsgi.application'

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
