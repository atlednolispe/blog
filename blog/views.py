# from silk.profiling.profiler import silk_profile

from blog.test_util import cache_it
from comment.models import Comment
from config.models import SideBar
from epsilon.models import Post, Category


class CommonMixin:
    # @silk_profile(name='get_category_context')
    @cache_it(60 * 5)
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