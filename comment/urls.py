from django.urls import path

from .views import CommentView, RecentComments


app_name = 'comment'
urlpatterns = [
    path('', CommentView.as_view(), name='index'),
    path('recently', RecentComments.as_view(), name='recent_comments'),
]

