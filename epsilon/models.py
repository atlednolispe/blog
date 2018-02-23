import markdown

from django.contrib.auth.models import User
from django.db import models
from django.db.models import F


class Post(models.Model):
    STATUS_ITEMS = (
        (1, '上线'),
        (2, '草稿'),
        (3, '删除'),
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    # Requires two positional arguments: to & on_delete
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="分类")

    tags = models.ManyToManyField('Tag', verbose_name="标签")
    content = models.TextField(verbose_name="内容", help_text="注: 目前仅支持Markdown格式数据")
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    is_markdown = models.BooleanField(verbose_name="使用markdown格式", default=True)
    content_html = models.TextField(verbose_name="markdown渲染后的数据", default='', blank=True)
    pv = models.PositiveIntegerField(default=0, verbose_name="pv")
    uv = models.PositiveIntegerField(default=0, verbose_name="uv")

    def __str__(self):
        """
        If not define __str__, the show in admin is XXX object(Num).
        """
        return self.title

    def show_tags(self):
        return ', '.join(str(t) for t in self.tags.all())
    show_tags.short_description = '标签'

    def increase_pv(self):
        return type(self).objects.filter(id=self.id).update(pv=F('pv') + 1)

    def increase_uv(self):
        return type(self).objects.filter(id=self.id).update(uv=F('uv') + 1)

    def save(self, *args, **kwargs):
        if self.is_markdown:
            config = {
                'codehilite': {
                    'use_pygments': False,
                    'css_class': 'prettyprint linenums',
                }
            }
            self.content_html = markdown.markdown(
                self.content,
                extensions=[
                    'codehilite',
                    'extra',
                    'toc',
                ],
                extension_configs=config
            )

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = verbose_name_plural = "文章"


class Category(models.Model):
    STATUS_ITEMS = (
        (1, '可用'),
        (2, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "分类"


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.BooleanField(default=True, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")

    desc = models.CharField(max_length=128, blank=True, verbose_name="简单描述")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'
