from django.contrib import admin

from blog.custom_admin import BaseOwnerAdmin
from blog.custom_site import custom_site

from .models import Link, SideBar


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'weight', 'owner')
    fields = ('title', 'href', 'weight')


@admin.register(SideBar, site=custom_site)
class SidebarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'owner')
    fields = ('title', 'display_type', 'content')
