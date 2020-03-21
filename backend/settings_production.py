from backend.settings import *
import django_heroku

DEBUG = False
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'fierce-shelf-18969.herokuapp.com']

STATICFILES_DIRS = [os.path.join(BASE_DIR, "build")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'static',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.prod.json')
    }
}

django_heroku.settings(locals())