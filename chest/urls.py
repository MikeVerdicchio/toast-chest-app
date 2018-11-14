from django.conf.urls import url
from chest import views, api

urlpatterns = [
    url(r'^$', views.chest, name='chest'),
    url(r'^random.json$', views.api_get_random, name='random-toast'),
]