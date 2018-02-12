from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from blog.custom_site import custom_site

from .models import Post, Category, Tag


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    # list_display = ('title', 'category', 'tags', 'status', 'owner', 'created_time',)
    list_display = (
        'title', 'category', 'show_tags', 'status',
        'owner', 'created_time', 'operator'
    )
    # search_fields = ['title', 'category', 'owner',]
    search_fields = ('title', 'category__name', 'owner__username',)

    list_filter = ('category', 'owner')
    save_on_top = True
    date_hierarchy = 'created_time'  # 时间的层级filter

    list_display_links = ('title', 'category')  # 可以通过点击字段到编辑页面
    list_editable = ('status',)  # 字段可编辑

    # fields = ('title', 'category',)  # 编辑页面展示哪些字段
    # 对编辑页面的更多定制, fields & fieldsets 二选一
    fieldsets = (
        ('基础配置', {
            'fields': (('title', 'category'), 'content')
        }),
        ('高级配置', {
            'classes': ('collapse',),  # 点击一次才展示
            'fields': ('tags', 'owner')
        }),
    )

    filter_horizontal = ('tags', )  # 左右箭头挑选
    # filter_vertical = ('tags', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('custom_site:epsilon_post_change', args=(obj.id,))
        )
    # operator.allow_tags = True  # 老版本用于转义html,现在用format_html替代
    operator.short_description = '操作'
    operator.empty_value_display = '???'  # 空值的默认展示


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass
