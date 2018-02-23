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

from django.urls import path, include
from xadmin.plugins import xversion

from epsilon.views import IndexView
from blog import adminx


xadmin.autodiscover()
xversion.register_models()  # revision & widget

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/', include('epsilon.urls')),
    path('config/', include('config.urls')),
    path('comment/', include('comment.urls')),
    path('admin/', xadmin.site.urls),  # admin & custom_admin removed
]
