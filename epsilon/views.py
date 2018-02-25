# import logging

from django.core.cache import cache
from django.views.generic import ListView, DetailView, TemplateView

from blog.views import CommonMixin
# from blog.test_util import time_it
from comment.views import CommentShowMixin

from .models import Post, Tag


# logger = logging.getLogger(__name__)


class BasePostView(CommonMixin, ListView):
    model = Post
    template_name = 'solid_state/elements.html'
    context_object_name = 'posts'
    paginate_by = 3
    ordering = '-id'


class IndexView(TemplateView):
    template_name = 'aerial/index.html'


class PostIndexView(BasePostView):
    # @time_it
    def get_queryset(self):
        query = self.request.GET.get('query')
        # logger.info('query: [%s]', query)
        qs = BasePostView.get_queryset(self)

        if query:
            qs = qs.filter(title__icontains=query)
        # logger.debug('query result: [%s]', qs)
        return qs

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super().get_context_data(query=query)


class CategoryView(BasePostView):
    def get_queryset(self):
        qs = BasePostView.get_queryset(self)
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostView):
    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []

        posts = tag.post_set.all()
        return posts


class PostView(CommonMixin, CommentShowMixin, DetailView):
    model = Post
    template_name = 'solid_state/generic.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):
        # self.object.pv += 1
        # self.object.uv += 1
        # self.object.save()

        sessionid = self.request.COOKIES.get('sessionid')
        if not sessionid:
            return

        pv_key = 'pv:%s:%s' % (sessionid, self.request.path)
        if not cache.get(pv_key):
            self.object.increase_pv()
            cache.set(pv_key, 1, 30)

        uv_key = 'uv:%s:%s' % (sessionid, self.request.path)
        if not cache.get(uv_key):
            self.object.increase_uv()
            cache.set(uv_key, 1, 60*60*24)



