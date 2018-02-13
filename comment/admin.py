from django.contrib import admin

from blog.custom_admin import BaseOwnerAdmin
from blog.custom_site import custom_site

from .models import Comment


@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_filter = ('email', 'status')
    search_fields = ('post__title', 'content')
    list_display = ('post', 'content', 'nickname', 'email')

    fieldsets = (
        ('基础配置', {
            'fields': ('post', 'content', 'status')
        }),
        ('高级配置', {
            'classes': ('collapse',),  # 点击一次才展示
            'fields': ('nickname', 'website', 'email')
        }),
    )
