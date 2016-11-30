from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^listing/item_edit/', views.item_edit),
    url(r'^listing/item/([0-9]+)', views.detail),
    url(r'^listing/all_items', views.listing),
]
