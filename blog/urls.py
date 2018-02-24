"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin

from django.conf import settings
from django.conf.urls.static import static  # collect staticfiles
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from xadmin.plugins import xversion

from blog import adminx
from epsilon.api import PostViewSet, CategoryViewSet, TagViewSet, UserViewSet
from epsilon.views import IndexView

from .autocomplete import CategoryAutocomplete, TagAutocomplete


xadmin.autodiscover()
xversion.register_models()  # revision & widget


router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'tag', TagViewSet)
router.register(r'user', UserViewSet)


urlpatterns = (
    [
        path('', IndexView.as_view(), name='index'),
        path('blog/', include('epsilon.urls')),
        path('config/', include('config.urls')),
        path('comment/', include('comment.urls')),
        path('admin/', xadmin.site.urls),  # admin & custom_admin removed
        path('category-autocomplete/', CategoryAutocomplete.as_view(), name='category-autocomplete'),
        path('tag-autocomplete/', TagAutocomplete.as_view(), name='tag-autocomplete'),
        path('ckeditor/', include('ckeditor_uploader.urls')),  # to replace ckeditor_uploader_urls.urlpatterns
        path('api/docs/', include_docs_urls(title='atlednolispe apis')),
        path('api/', include(router.urls)),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)  # url is likely to be deprecated in a future release.
