from django.urls import path
from django.conf.urls import url

from . import views

#URL中要用‘/’
#app_name='myapp'  很重要
app_name = 'leaveschoolregistration'
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^leaveschooltlist/$', views.leaveschooltlist,name='leaveschooltlist'),
    url(r'^login/$', views.login,name='login'),
]