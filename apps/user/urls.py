
from django.conf.urls import url
from .views import *

app_name = 'user'

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="user_login"),
    url(r'^hola/$', test.as_view(), name="hola"),
    url(r'^logout/$', logout, name="user_logout"),
]
