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

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super(Post, self).save(*args, **kwargs)
        if is_new:
            self.on_post_create()

    # TODO: Write real method for send notifications to scribers
    # TODO: Rewrite with using celery
    def on_post_create(self):
        if self.pk is None:
            return
        subscription_set = self.author.subscription_set.all()
        for subscription in subscription_set:
            Feed(post=self, subscriber=subscription.subscriber, subscription=subscription).save()
            print('\tSend message to', subscription.subscriber, subscription.subscriber.email)

    def __str__(self):
        return '{0} {1} {2}'.format(self.create_at, self.author, self.title)

    class Meta:
        verbose_name_plural = _('posts items')
        verbose_name = _('post item')
        ordering = ['-create_at', ]


class Subscription(models.Model):

    author = models.ForeignKey(
        User,
        verbose_name=_('author'),
        related_name='subscription_set',
    )
    subscriber = models.ForeignKey(
        User,
        verbose_name=_('subscriber'),
        related_name='+',
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super(Subscription, self).save(*args, **kwargs)
        if is_new:
            self.on_subscription_create()

    # TODO: Rewrite with using celery
    def on_subscription_create(self):
        for post in self.author.post_set.all():
            Feed(post=post, subscriber=self.subscriber, subscription=self).save()

    class Meta:
        verbose_name_plural = _('subscriptions items')
        verbose_name = _('subscription item')
        unique_together = (('author', 'subscriber'),)


class Feed(models.Model):

    post = models.ForeignKey(
        Post,
        verbose_name=_('post'),
    )
    subscriber = models.ForeignKey(
        User,
        verbose_name=_('subscriber'),
    )
    is_red = models.BooleanField(
        verbose_name=_('post is red'),
        default=False,
    )
    subscription = models.ForeignKey(
        Subscription,
        verbose_name=_('subscription item'),
    )

    class Meta:
        verbose_name_plural = _('feed items')
        verbose_name = _('feed item')
        unique_together = (('post', 'subscriber'),)
        ordering = ('-post__create_at', )
