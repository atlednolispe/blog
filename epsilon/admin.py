from django.contrib import admin

from .models import Post, Category, Tag
from blog.custom_site import custom_site


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    # list_display = ('title', 'category', 'tags', 'status', 'owner', 'created_time',)
    list_display = ('title', 'category', 'show_tags', 'status', 'owner', 'created_time',)
    # search_fields = ['title', 'category', 'owner',]
    search_fields = ['title', 'category__name', 'owner__username', ]

    list_filter = ('category', 'owner')
    save_on_top = True


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass
