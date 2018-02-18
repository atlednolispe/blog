from django.urls import path

from .views import LinkView


app_name = 'config'
urlpatterns = [
    path('links/', LinkView.as_view(), name='links'),
]
