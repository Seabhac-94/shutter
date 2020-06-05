from django.conf.urls import url
from .views import all_products, irishness_products, nature_products, still_life_products, adventure_products

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^still_life', still_life_products, name='still_life_products'),
    url(r'^adventure', adventure_products, name='adventureproducts'),
    url(r'^nature', nature_products, name='natureproducts'),
    url(r'^irishness', irishness_products, name='irishproducts')
]