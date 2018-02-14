from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from config.models import SideBar
from comment.models import Comment

from .models import Post, Tag, Category


def get_common_context():
    categories = Category.objects.filter(status=1)  # filter '可用'
    nav_cates = [cate for cate in categories if cate.is_nav]
    none_nav_cates = [cate for cate in categories if not cate.is_nav]

    side_bars = SideBar.objects.filter(status=1)  # fliter展示
    recent_posts = Post.objects.filter(status=1).order_by('-created_time')[:3]
    # hot_posts = Post.objects.filter(status=1).order_by('-views')[:3]
    recent_comments = Comment.objects.filter(status=1).order_by('-created_time')[:3]

    context = {
        'nav_cates': nav_cates,
        'none_nav_cates': none_nav_cates,
        'side_bars':side_bars,
        'recent_posts': recent_posts,
        'recent_comments': recent_comments
    }
    return context


def post_list(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()
    page = request.GET.get('page', 1)  # ?page=2
    per_page = 3

    try:
        page = int(page)
    except TypeError:
        page = 1

    if category_id:
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.post_set.all()

    queryset = queryset.order_by('-id')
    paginator = Paginator(queryset, per_page)
    post = paginator.get_page(page)

    context = {
        'posts': post,
    }
    common_context = get_common_context()
    context.update(common_context)

    return render(request, 'epsilon/list.html', context=context)


def post_detail(request, id=None):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Post doesn't exist!")

    context = {
        'post': post
    }
    common_context = get_common_context()
    context.update(common_context)

    return render(request, 'epsilon/detail.html', context=context)
