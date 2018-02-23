import xadmin

from blog.adminx import BaseOwnerAdmin

from .models import Comment


class CommentAdmin(BaseOwnerAdmin):
    list_filter = ('email', 'status')
    search_fields = ('target', 'content')
    list_display = ('target', 'content', 'nickname', 'email')

    fieldsets = (
        ('基础配置', {
            'fields': ('target', 'content', 'status')
        }),
        ('高级配置', {
            'classes': ('collapse',),  # 点击一次才展示
            'fields': ('nickname', 'website', 'email')
        }),
    )


xadmin.site.register(Comment, CommentAdmin)

