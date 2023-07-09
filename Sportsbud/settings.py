from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b-+*k@nc$!_%lctf_s_lrjnm%dcbcs!43$=ljg!za_#qxi7gtd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 正常情况下生产环境debug一定要False，不过这个web不重要，turn True的话heroku就可以存储media文件而不用aws s3了。

ALLOWED_HOSTS = ['huskysports.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'baseapp.apps.BaseappConfig',

    'rest_framework', 
    'corsheaders',

    'storages', # AWS S3 bucket storage
]

AUTH_USER_MODEL = 'baseapp.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Sportsbud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # BASE_DIR / 'reactapp/build',
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Sportsbud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#---- MicroSoft SQL Server Database (mssql-django)
DATABASES = {
    'default': {
        'ENGINE': 'mssql',  
        'NAME': os.getenv("DBName"),
        'HOST': os.getenv("Host"), 
        'PORT': os.getenv("Port"), 
        'USER': os.getenv("UserID"),  
        'PASSWORD': os.getenv("Password"), 
    }
}

# ---- Default SQLite database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#   }
#}


# ---- MySQL databse (pymysql, imported in _init_.py)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  
#         'NAME': os.getenv("DBName"),
#         'HOST': os.getenv("Host"), 
#         'PORT': os.getenv("Port"), 
#         'USER': os.getenv("UserID"),  
#         'PASSWORD': os.getenv("Password"), 
#     }
# }
 

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# --- if not using AWS S3
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles' 
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOW_ALL_ORIGINS = True


# --- S3 BUCKETS CONFIGURE
AWS_ACCESS_KEY_ID = 'AKIA4DVZ4GUFSMQMXQWX'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'nick-first-bucket'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

STATIC_LOCATION = 'static' 
STATIC_URL = f'https://nick-first-bucket.s3.amazonaws.com/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'Sportsbud.storage_backends.StaticStorage'

MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://nick-first-bucket.s3.amazonaws.com/{MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'Sportsbud.storage_backends.MediaStorage'

# AWS S3 bucket CORS configuration
'''
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "POST",
            "GET",
            "PUT"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
'''