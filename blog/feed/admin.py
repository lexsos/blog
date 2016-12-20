from django.contrib import admin
from django.conf import settings

from .models import Post, Subscription, Feed


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('create_at', 'author', 'title')


class SubscriptionAdmin(admin.ModelAdmin):
    list_filter = ('author', 'subscriber')
    list_display = ('subscriber', 'author')


class FeedAdmin(admin.ModelAdmin):
    list_filter = ('subscriber', )
    list_display = ('post', 'subscriber', 'is_red')


admin.site.register(Post, PostAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
if settings.DEBUG:
    admin.site.register(Feed, FeedAdmin)
