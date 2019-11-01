import dj_database_url
import django_heroku

from toast_chest.base import *

DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600)

# Activate Django-Heroku.
django_heroku.settings(locals())
