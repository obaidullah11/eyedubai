"""
Django settings for eyedubai project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

import firebase_admin
from firebase_admin import credentials,initialize_app
from firebase_admin.exceptions import FirebaseError
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# service_account_json = os.path.join(BASE_DIR, 'eyedubai', 'adminsdk.json')
# try:
#     cred = credentials.Certificate(service_account_json)
#     firebase_app = initialize_app(cred)
#     print("Firebase connected successfully")
# except FirebaseError as e:
#     print("Failed to connect to Firebase:", e)




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-za72^!nk_jf^uj=#w4!(o*h7!nf*)t1s&54sbtou)z_=5e+*$t'


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Update with your SMTP server address
EMAIL_PORT = 587  # Update with your SMTP server port (587 for TLS)
EMAIL_USE_TLS = True  # Set to True if your SMTP server requires TLS
EMAIL_HOST_USER = 'coppercool1234@gmail.com'  # Update with your SMTP username
EMAIL_HOST_PASSWORD = 'cvfp dthd yqat dwxa'  # Update with your SMTP password









# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    # 'eyedubaiproducts',
    # 'notifications',


    # 'products',
    # 'import_export',
    # 'adminsortable2',
    'users',
    # 'interests',
    # 'Events',
    # 'factory',
    # 'importer',
    # 'vehicles',
    # 'Garage',
    # 'Maintenance',
    'sslserver',

    # 'eyedubai_Admin',
    # 'sortedm2m',

    # 'dealer',
    # 'dealers',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eyedubai.urls'

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

WSGI_APPLICATION = 'eyedubai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'django',
    }
}

AUTH_USER_MODEL ='users.User'
# AUTHENTICATION_BACKENDS = ['users.backends.EmailBackend']
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/
MAX_UPLOAD_SIZE = "429916160"
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../', 'static')
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     os.path.join(BASE_DIR, '../', 'static')
# ]
# STATICFILES_DIRS = [
#     'E:/Express car rentel/../static',
# ]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=20),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),



    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
}
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ['*']


JAZZMIN_UI_TWEAKS = {
     "sidebar_fixed": True,
}
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "eyedubai Administration",
    "site_header": "eyedubai",
    "site_brand": "eyedubai",
    "copyright": "eyedubai",
    "show_ui_builder":True,
    "order_with_respect_to": ["auth","accounts","accounts.user","accounts.country","evaluation","evaluation.evaluate","evaluation.feature_car","products","products.acesories",
                              "products.features","products.category","products.product","products.postimage",
                              "products.auction","products.bidding","products.wishlist","products.Car_legends",
                              "products.wheelsimage","products.vehicle_information",
                              "products.inspection_title","products.inspection_subtitle",
                              "products.inspection_question","products.inspection_choice",
                              "products.Inspection_car"],

    "icons": {
        "auth": "fas fa-users-cog",
        "accounts.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "accounts.balance": "fas fa-euro-sign",
        "accounts.balance_history": "fas fa-history",
        "products.product":'fas fa-car-side',
        # "products.newSparePart":'fa fa-heart',
"products.bidding":'fa fa-gavel',
"products.auction":'fa fa-hand-holding-usd',
"products.category":'fa fa-align-center',
"products.acesories":'fa fa-list',
"products.features":'fa fa-tasks',
    },
    "hide_models": ['auth.group',],
"hide_apps": ['knox'],
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "products"},
    ],
"related_modal_active": True
}
X_FRAME_OPTIONS = 'SAMEORIGIN'
USE_DJANGO_JQUERY = True
