from django.conf.urls import url, include
from accounts.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]