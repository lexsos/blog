from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import FeedView, PostCreate


urlpatterns = [
    url(r'^feed/$', FeedView.as_view(), name='blog_feed'),
    url(r'^new_post/$', PostCreate.as_view(), name='blog_create_post'),
    url(r'^login/$', auth_views.login, {'template_name': 'feed/login.html'}, name='login'),
]