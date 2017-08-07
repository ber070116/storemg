
from django.conf.urls import url
from .views import *

app_name = 'store'

urlpatterns = [
    url(r'', StoreListView.as_view(), name="index"),
]
