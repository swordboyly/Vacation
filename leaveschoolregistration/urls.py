from django.urls import path
from django.conf.urls import url

from . import views

#URL��Ҫ�á�/��
#app_name='myapp'  ����Ҫ
app_name = 'leaveschoolregistration'
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^leaveschooltlist/$', views.leaveschooltlist,name='leaveschooltlist'),
    url(r'^login/$', views.login,name='login'),
]