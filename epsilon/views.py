from django.shortcuts import render


def post_list(request, category_id=None, tag_id=None):
    context = {
        'name': 'post_list',
        'tag_id': tag_id
    }
    return render(request, 'epsilon/list.html', context=context)


def post_detail(request, post_id=None):
    context = {
        'name': 'post_detail'
    }
    return render(request, 'epsilon/detail.html', context=context)