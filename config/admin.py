from django.contrib import admin

from blog.custom_site import custom_site

from .models import Link, SideBar


@admin.register(Link, site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'weight', 'owner')


@admin.register(SideBar, site=custom_site)
class SidebarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'owner')
