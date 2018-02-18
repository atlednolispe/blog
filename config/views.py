from django.views.generic import ListView

from epsilon.views import CommonMixin

from .models import Link


class LinkView(CommonMixin, ListView):
    queryset = Link.objects.filter(status=1)
    template_name = 'solid_state/links.html'
    context_object_name = 'links'
    ordering = '-weight'
