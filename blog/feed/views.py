from django.views.generic.list import ListView

from .models import Feed


class FeedView(ListView):

    model = Feed

    def get_queryset(self, *args, **kwargs):
        queryset = super(FeedView, self).get_queryset(*args, **kwargs)
        if self.request.user.is_authenticated():
            queryset = queryset.filter(subscriber=self.request.user)
        return queryset
