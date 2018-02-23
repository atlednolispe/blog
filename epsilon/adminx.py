import xadmin

from django.utils.html import format_html
from django.urls import reverse
from xadmin.layout import Fieldset, Row

from blog.adminx import BaseOwnerAdmin

from .models import Post, Category, Tag
from .adminforms import PostAdminForm, TagAdminForm


class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = (
        'title', 'category', 'show_tags', 'status',
        'pv', 'uv', 'created_time', 'operator'
    )
    exclude = ('html', 'owner', 'pv', 'uv')
    search_fields = ('title', 'category__name')

    list_filter = ('category',)
    save_on_top = True
    date_hierarchy = 'created_time'  # 时间的层级filter

    form_layout = (
        # Fieldset(
        #     ('基础配置', {
        #         'fields': (Row('title', 'category'), 'is_markdown',
        #                    'content', 'desc')
        #     }),
        #     ('高级配置', {  # post can't be showed
        #         'classes': ('collapse',),  # 点击一次才展示
        #         'fields': ('tags',)
        #     }),
        # )
        Fieldset(
            '基础配置',
            'title', Row('category', 'status'),
            'is_markdown', 'content', 'desc', 'tags',
        )
    )

    filter_horizontal = ('tags', )  # 左右箭头挑选

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('custom_site:epsilon_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'
    operator.empty_value_display = '???'  # 空值的默认展示


xadmin.site.register(Post, PostAdmin)  # change decorator to site.register


class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')


xadmin.site.register(Category, CategoryAdmin)


class TagAdmin(BaseOwnerAdmin):
    form = TagAdminForm
    fields = ('name', 'status', 'desc')
    list_display = ('name', 'status', 'desc', 'created_time')


xadmin.site.register(Tag, TagAdmin)
