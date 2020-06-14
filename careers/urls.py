from django.conf.urls import url
from .views import current_jobs, apply

urlpatterns = [
    url(r'^$', current_jobs, name='careers'),
    url(r'^apply', apply, name='apply')
]