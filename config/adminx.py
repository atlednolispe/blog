import xadmin

from blog.adminx import BaseOwnerAdmin

from .models import Link, SideBar


class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'weight', 'owner')
    fields = ('title', 'href', 'weight')


xadmin.site.register(Link, LinkAdmin)


class SidebarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'owner')
    fields = ('title', 'display_type', 'content')


xadmin.site.register(SideBar, SidebarAdmin)
