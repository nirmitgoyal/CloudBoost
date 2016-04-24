from django.conf.urls import include, url
from django.contrib import admin
from . import views
app_name = 'elasticsearch_and_redis_app'

urlpatterns = [
    # ex: /cloudboost/
    url(r'^$', views.cloudboost, name='cloudboost'),
    # ex: /cloudboost/index/    
    url(r'^index/$', views.index, name='index'),
    # ex: /cloudboost/search/
    url(r'^search/$', views.search, name='search'),    
]
