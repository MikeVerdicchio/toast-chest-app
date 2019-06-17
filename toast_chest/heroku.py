from toast_chest.base import *
import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
