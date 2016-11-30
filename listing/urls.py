from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^listing/item_new', views.item_new, name="item_new"),
    url(r'^listing/(?P<pk>[0-9]+)/edit/$', views.item_edit, name="item_edit"),
    url(r'^listing/(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name="item_delete"),
    url(r'^listing/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="item_detail"),
    url(r'^listing/all_items', views.ListingView.as_view(), name="item_list"),
]
