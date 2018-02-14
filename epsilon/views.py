from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from .models import Post, Tag


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
        'posts': post
    }
    return render(request, 'epsilon/list.html', context=context)


def post_detail(request, id=None):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Post doesn't exist!")

    context = {
        'post': post
    }
    return render(request, 'epsilon/detail.html', context=context)
