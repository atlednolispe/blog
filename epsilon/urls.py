from django.views.decorators.cache import cache_page
from django.urls import path

from .views import PostIndexView, PostView, CategoryView, TagView


app_name = 'epsilon'
urlpatterns = [
    path('', cache_page(60 * 10)(PostIndexView.as_view()), name='index'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag'),
    path('post/<int:pk>/', PostView.as_view(), name='detail'),
]
