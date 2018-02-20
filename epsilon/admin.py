from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from blog.custom_admin import BaseOwnerAdmin
from blog.custom_site import custom_site

from .models import Post, Category, Tag
from .adminforms import TagAdminForm


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    list_display = (
        'title', 'category', 'show_tags', 'status',
        'pv', 'uv', 'created_time', 'operator'
    )
    search_fields = ('title', 'category__name')

    list_filter = ('category',)
    save_on_top = True
    date_hierarchy = 'created_time'  # 时间的层级filter

    fieldsets = (
        ('基础配置', {
            'fields': (('title', 'category'), 'is_markdown', 'content')
        }),
        ('高级配置', {
            'classes': ('collapse',),  # 点击一次才展示
            'fields': ('tags',)
        }),
    )

    filter_horizontal = ('tags', )  # 左右箭头挑选

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('custom_site:epsilon_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'
    operator.empty_value_display = '???'  # 空值的默认展示


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    form = TagAdminForm
    fields = ('name', 'status', 'desc')
    list_display = ('name', 'status', 'desc', 'created_time')
