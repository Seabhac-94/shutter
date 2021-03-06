from django.conf.urls import url
from .views import all_products, irishness_products, nature_products, still_life_products, adventure_products, collections

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^collections', collections, name='collections'),
    url(r'^still_life', still_life_products, name='still_life'),
    url(r'^adventure', adventure_products, name='adventure'),
    url(r'^nature', nature_products, name='nature'),
    url(r'^irishness', irishness_products, name='irish')
]
