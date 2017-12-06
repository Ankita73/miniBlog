from django.conf.urls import url
from django.contrib import admin

from .views import (
    BlogListAPIView,
    BlogDetailAPIView,
    BlogUpdateAPIView,
    BlogDestroyAPIView,
    BlogCreateAPIView,
    )

app_name = 'blog'

urlpatterns = [
    url(r'^$', BlogListAPIView.as_view(), name='list'),
    url(r'^create/$', BlogCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', BlogDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', BlogUpdateAPIView.as_view(), name='Update'),
    url(r'^(?P<pk>\d+)/delete/$', BlogDestroyAPIView.as_view(), name='delete'),
]