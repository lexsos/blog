from django.conf.urls import url

from .views import FeedView


urlpatterns = [
    url(r'^feed/$', FeedView.as_view(), name='blog_feed'),
]