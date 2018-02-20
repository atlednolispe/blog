from django.views.generic import ListView, DetailView, TemplateView

from config.models import SideBar
from comment.views import CommentShowMixin
from comment.models import Comment

from .models import Post, Tag, Category


class CommonMixin:
    def get_category_context(self):
        categories = Category.objects.filter(status=1)  # filter '可用'
        nav_cates = [cate for cate in categories if cate.is_nav]
        none_nav_cates = [cate for cate in categories if not cate.is_nav]

        return {
            'nav_cates': nav_cates,
            'none_nav_cates': none_nav_cates
        }

    def get_context_data(self, **kwargs):
        side_bars = SideBar.objects.filter(status=1)  # fliter展示
        recent_posts = Post.objects.filter(status=1).order_by('-created_time')[:3]
        hot_posts = Post.objects.filter(status=1).order_by('-pv')[:3]
        recent_comments = Comment.objects.filter(status=1).order_by('-created_time')[:3]

        context = {
            'side_bars': side_bars,
            'recent_posts': recent_posts,
            'recent_comments': recent_comments,
            'hot_posts': hot_posts,
        }
        kwargs.update(self.get_category_context())
        kwargs.update(context)

        return super().get_context_data(**kwargs)


class BasePostView(CommonMixin, ListView):
    model = Post
    template_name = 'solid_state/elements.html'
    context_object_name = 'posts'
    paginate_by = 1
    ordering = '-id'


class IndexView(TemplateView):
    template_name = 'aerial/index.html'


class PostIndexView(BasePostView):
    def get_queryset(self):
        query = self.request.GET.get('query')
        qs = BasePostView.get_queryset(self)

        if query:
            qs = qs.filter(title__icontains=query)
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

        self.object.increase_pv()
        self.object.increase_uv()



