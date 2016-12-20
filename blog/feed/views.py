from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Feed, Subscription, Post
from .forms import PostCreateForm


class LoginUrlMixin(object):

    def get_login_url(self):
        return reverse('login')


class FeedView(LoginUrlMixin, LoginRequiredMixin, ListView):

    model = Feed

    def get_queryset(self):
        queryset = super(FeedView, self).get_queryset()
        if self.request.user.is_authenticated():
            queryset = queryset.filter(subscriber=self.request.user)
        return queryset


class PostCreate(LoginUrlMixin, LoginRequiredMixin, FormView):

    template_name = 'feed/post_create.html'
    form_class = PostCreateForm

    def get_success_url(self):
        return reverse('blog_feed')

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
        return super(PostCreate, self).form_valid(form)


class AuthorListView(LoginUrlMixin, LoginRequiredMixin, ListView):
    template_name = 'feed/authors_list.html'
    model = User


class SubscribeView(LoginUrlMixin, LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('blog_authors_list')

    def post(self, request, *args, **kwargs):
        try:
            author = User.objects.get(pk=kwargs.get('author_id', -1))
            subscriber = self.request.user
            if subscriber.is_authenticated():
                Subscription.objects.get_or_create(author=author, subscriber=subscriber)
        except User.DoesNotExist:
            pass
        return super(SubscribeView, self).post(request, *args, **kwargs)


class UnsubscribeView(LoginUrlMixin, LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('blog_authors_list')

    def post(self, request, *args, **kwargs):
        try:
            author = User.objects.get(pk=kwargs.get('author_id', -1))
            subscriber = self.request.user
            if subscriber.is_authenticated():
                Subscription.objects.filter(author=author, subscriber=subscriber).delete()
        except User.DoesNotExist:
            pass
        return super(UnsubscribeView, self).post(request, *args, **kwargs)


class MarkReadView(LoginUrlMixin, LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('blog_feed')

    def post(self, request, *args, **kwargs):
        try:
            post = Post.objects.get(pk=kwargs.get('post_id', -1))
            subscriber = self.request.user
            if subscriber.is_authenticated():
                Feed.objects.filter(post=post, subscriber=subscriber).update(is_red=True)
        except Post.DoesNotExist:
            pass
        return super(MarkReadView, self).post(request, *args, **kwargs)
