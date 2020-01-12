from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url('all/', UsersListView.as_view()),
    url(r'^user/(?P<user>[0-9]+)/$', userStatListView),
    url(r'^user/(?P<user>[0-9]+)/(?P<firstData>.+)/(?P<lastData>.+)/$', userStatListDateView),
]