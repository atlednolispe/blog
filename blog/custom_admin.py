from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    针对有owner属性的数据, 重写:
    1. save_model - 保证每条数据属于当前用户
    2. get_queryset- 保证每个用户只能看到自己的文章
    """
    def get_queryset(self, request):
        qs = admin.ModelAdmin.get_queryset(self, request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        admin.ModelAdmin.save_model(self, request, obj, form, change)
