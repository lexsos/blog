from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Post, Subscription, ViewMark


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('create_at', 'author', 'title')


class SubscriptionAdmin(admin.ModelAdmin):
    list_filter = ('author', 'subscriber')
    list_display = ('subscriber', 'author')


class ViewMarkAdmin(admin.ModelAdmin):
    list_filter = ('subscriber', )
    list_display = ('subscriber', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(ViewMark, ViewMarkAdmin)