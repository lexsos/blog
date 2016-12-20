from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import (
    FeedView,
    PostCreate,
    AuthorListView,
    SubscribeView,
    UnsubscribeView,
)


urlpatterns = [
    url(r'^feed/$',
        FeedView.as_view(),
        name='blog_feed',
        ),
    url(r'^new_post/$',
        PostCreate.as_view(),
        name='blog_create_post',
        ),
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'feed/login.html'},
        name='login',
        ),
    url(r'^logout/$',
        auth_views.logout,
        name='logout',
        ),
    url(r'^authors/$',
        AuthorListView.as_view(),
        name='blog_authors_list',
        ),
    url(r'^subscribe/(?P<pk>\d+)/$',
        SubscribeView.as_view(),
        name='blog_subscribe',
        ),
    url(r'^unsubscribe/(?P<pk>\d+)/$',
        UnsubscribeView.as_view(),
        name='blog_unsubscribe',
        ),
]
