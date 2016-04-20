from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # ex: /cloudboost/
    url(r'^$', views.index, name='cloudboost'),
    # ex: /cloudboost/index/    
    url(r'^index/$', views.index, name='index'),
    # ex: /cloudboost/search/
    url(r'^search/$', views.search, name='search'),    
]
