from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Feed
from .forms import PostCreateForm


class FeedView(LoginRequiredMixin, ListView):

    model = Feed

    def get_queryset(self):
        queryset = super(FeedView, self).get_queryset()
        if self.request.user.is_authenticated():
            queryset = queryset.filter(subscriber=self.request.user)
        return queryset

    def get_login_url(self):
        return reverse('login')


class PostCreate(LoginRequiredMixin, FormView):

    template_name = 'feed/post_create.html'
    form_class = PostCreateForm

    def get_success_url(self):
        return reverse('blog_feed')

    def get_login_url(self):
        return reverse('login')

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
        return super(PostCreate, self).form_valid(form)
