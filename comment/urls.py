from django.urls import path

from .views import CommentView


app_name = 'comment'
urlpatterns = [
    path('', CommentView.as_view(), name='index'),
]