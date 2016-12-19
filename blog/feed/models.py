from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _



class Post(models.Model):

    title = models.CharField(
        verbose_name=_('post title'),
        max_length=255,
    )
    content = models.TextField(
        verbose_name=_('post content'),
    )
    create_at = models.DateTimeField(
        verbose_name=_('post create date'),
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name=_('post author'),
    )

    class Meta:
        verbose_name_plural = _('posts items')
        verbose_name = _('post item')
        ordering = ['-create_at', ]


class Subscription(models.Model):

    author = models.ForeignKey(
        User,
        verbose_name=_('author'),
        related_name='subscription_authors_set',
    )
    subscriber = models.ForeignKey(
        User,
        verbose_name=_('subscriber'),
        related_name='subscription_subscriber_set',
    )

    class Meta:
        verbose_name_plural = _('subscriptions items')
        verbose_name = _('subscription item')
        unique_together = (('author', 'subscriber'),)


class ViewMark(models.Model):

    post = models.ForeignKey(
        Post,
        verbose_name=_('post'),
    )
    subscriber = models.ForeignKey(
        User,
        verbose_name=_('subscriber'),
    )

    class Meta:
        verbose_name_plural = _('view marks items')
        verbose_name = _('view mark item')
        unique_together = (('post', 'subscriber'),)