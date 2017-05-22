from django.conf.urls import url
from django.contrib import admin
from . import views 
urlpatterns = [

    url(r'^$', view.data_list,name="list")
]