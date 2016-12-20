from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import (
    FeedView,
    PostCreate,
    AuthorListView,
    SubscribeView,
    UnsubscribeView,
    MarkReadView,
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
    url(r'^subscribe/(?P<author_id>\d+)/$',
        SubscribeView.as_view(),
        name='blog_subscribe',
        ),
    url(r'^unsubscribe/(?P<author_id>\d+)/$',
        UnsubscribeView.as_view(),
        name='blog_unsubscribe',
        ),
    url(r'^mark_read/(?P<post_id>\d+)/$',
        MarkReadView.as_view(),
        name='blog_mark_read',
        ),
]
