import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'times.apps.TimesConfig',
    'vacancies.apps.VacanciesConfig',
    'lessons.apps.LessonsConfig',
    'addresses.apps.AddressesConfig',
    'cafes.apps.CafesConfig',
    'corsheaders',
    'phonenumber_field',
    'rest_framework',
    'rest_framework_swagger',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'main.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'daqv0io2efdfe7',
#         'USER': 'clzaxzyucwfjcm',
#         'PASSWORD': '1b20449a267da5008edc5cf1d31e1ab873cd733a62e3bd3df2930fe04618bdad',
#         'HOST': 'ec2-52-214-23-110.eu-west-1.compute.amazonaws.com',
#         'PORT': 5432
#     }
# }
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}


AUTH_PWD_MODULE = 'django.contrib.auth.password_validation.'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'{AUTH_PWD_MODULE}UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'{AUTH_PWD_MODULE}MinimumLengthValidator',
    },
    {
        'NAME': f'{AUTH_PWD_MODULE}CommonPasswordValidator',
    },
    {
        'NAME': f'{AUTH_PWD_MODULE}NumericPasswordValidator',
    },
]

SITE_ID = 1

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ALLOW_ALL_ORIGINS = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'