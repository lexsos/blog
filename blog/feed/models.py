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
        subscription_set = None
        if not self.pk:
            subscription_set = self.author.subscription_set.all()

        super(Post, self).save(*args, **kwargs)
        # TODO: write real method for send notifications to scribers
        if subscription_set:
            print ('Create new post id:', self.pk)
            print('Send messages to scribers:')
            for subscription in subscription_set:
                print('\tSend message to ', subscription.subscriber, ' ', subscription.subscriber.email)

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
