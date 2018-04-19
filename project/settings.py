import os, string, random, lamarziendan

try:
    import uwsgi
    SECRET_KEY = ''.join(random.choice(string.printable) for x in range(50))
    DEBUG = False
except ImportError:
    SECRET_KEY = 'abc'
    DEBUG = True

ADMINS = [('JJ Vens', 'jj@rtts.eu')]
ALLOWED_HOSTS = ['*']
WSGI_APPLICATION = 'project.wsgi.application'
ROOT_URLCONF = 'lamarziendan.urls'
LANGUAGE_CODE = 'nl'
TIME_ZONE = 'Europe/Amsterdam'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = '/srv/lamarziendan/static'
MEDIA_ROOT = '/media/'
MEDIA_ROOT = '/srv/lamarziendan/media'
SASS_PROCESSOR_ROOT = os.path.join(os.path.dirname(os.path.abspath(lamarziendan.__file__)), 'static')

INSTALLED_APPS = [
    'lamarziendan',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sass_processor',
    'embed_video',
    'ckeditor',
    'easy_thumbnails',
]

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'lamarziendan',
        'NAME': 'lamarziendan',
    }
}
