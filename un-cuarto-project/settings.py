import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env()

# Quick-start development un-cuarto-project - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ


DJANGO_SUPERUSER_PASSWORD=env('DJANGO_SUPERUSER_PASSWORD')
DJANGO_SUPERUSER_USERNAME=env('DJANGO_SUPERUSER_USERNAME')
DJANGO_SUPERUSER_FIRST_NAME=env('DJANGO_SUPERUSER_FIRST_NAME')
DJANGO_SUPERUSER_LAST_NAME=env('DJANGO_SUPERUSER_LAST_NAME')
DJANGO_SUPERUSER_EMAIL=env('DJANGO_SUPERUSER_EMAIL')


ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

HTTP_ACCEPT_ENCODING="gzip"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'un_cuarto',
    'sri',
    'csp'
]

CRISPY_TEMPLATE_PACK='bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'un-cuarto-project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'csp.context_processors.nonce',
            ],
        },
    },
]

WSGI_APPLICATION = 'un-cuarto-project.wsgi.application'

X_FRAME_OPTIONS = 'DENY'


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': env('DATABASE_NAME'),
         'USER': env('DATABASE_USER'),
         'PASSWORD': env('DATABASE_PASSWORD'),
         'HOST': env('DATABASE_HOST'),
         'PORT': env('DATABASE_PORT'),
     }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSP_DEFAULT_SRC="'self'"
CSP_STYLE_SRC = ["'self'",]
CSP_IMG_SRC = ("'self'",
    # "i.ytimg.com/",
	# "www.google-analytics.com",
	# "googleads.g.doubleclick.net",
    )
CSP_SCRIPT_SRC = ("'self'",
    # "cdn.plyr.io/3.6.12/plyr.js",
    "www.youtube.com",
    # "www.youtube.com/iframe_api",
    # "www.youtube.com/s/player/03bec62d/www-widgetapi.vflset/www-widgetapi.js"
	# "ajax.cloudflare.com",
	# "static.cloudflareinsights.com",
	# "www.google-analytics.com",
	# "ssl.google-analytics.com",
    # "cdnjs.cloudflare.com",
    # "www.google.com/recaptcha/api.js",
	# "pagead2.googlesyndication.com",
    )
CSP_FONT_SRC=("'self'", 'data:')
CSP_CONNECT_SRC = ["'none'",
    # "www.google-analytics.com"
    ]
CSP_OBJECT_SRC="'none'"
CSP_BASE_URI="'none'"
CSP_FRAME_SRC=["'self'",
# "www.google.com",
"www.youtube.com",
# "www.youtube-nocookie.com"
]
CSP_FRAME_ANCESTORS="'self'"
CSP_FORM_ACTION="'self'"
CSP_INCLUDE_NONCE_IN=["script-src", "style-src",]
# CSRF_COOKIE_SAMESITE = 'Strict'
# UPGRADE_INSECURE_REQUESTS = True
# CSP_REPORT_URI = 'http://127.0.0.1:8000/'
# loading manifest, workers, frames, etc
CSP_MANIFEST_SRC = ("'self'", )
CSP_WORKER_SRC = ("'self'", )
CSP_MEDIA_SRC = ("'self'",
# "www.dropbox.com",
)

DEFAULT_FROM_EMAIL = 'webuncuarto@gmail.com'

USE_SRI=True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if not DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_USE_TLS = env('EMAIL_USE_TLS')
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_HTTPONLY = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    # SECURE_REDIRECT_EXEMPT = []
    ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    

    # # django-ckeditor will not work with S3 through django-storages without this line in settings.py
    # AWS_QUERYSTRING_AUTH = False

    # # aws settings

    # AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    # AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

    # AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    # AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # AWS_DEFAULT_ACL = 'public-read'

    # # s3 static settings
    # STATIC_LOCATION = 'static'
    # STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # # s3 public media settings

    # PUBLIC_MEDIA_LOCATION = 'media'
    # MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    # DEFAULT_FILE_STORAGE = 'core.storage_backends.MediaStore'
