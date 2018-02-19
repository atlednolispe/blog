from django.views.generic import ListView

from comment.forms import CommentForm
from epsilon.views import CommonMixin

from .models import Link


class LinkView(CommonMixin, ListView):
    queryset = Link.objects.filter(status=1)
    template_name = 'solid_state/links.html'
    context_object_name = 'links'
    ordering = '-weight'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(),
        })
        return super().get_context_data(**kwargs)
