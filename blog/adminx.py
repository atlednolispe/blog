import xadmin

from xadmin.views import CommAdminView


class BaseOwnerAdmin:
    """
    针对有owner属性的数据, 重写:
    1. save_model - 保证每条数据属于当前用户
    2. get_queryset- 保证每个用户只能看到自己的文章
    """
    def get_list_queryset(self):  # get_query_set(self, request) --> get_list_queryset(self)
        request = self.request

        qs = super().get_list_queryset()
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_models(self):  # save_model(self, request, obj, form, change) --> save_models(self)
        if not self.org_obj:
            self.new_obj.owner = self.request.user

        return super().save_models()


class GlobalSetting(CommAdminView):
    site_title = 'Epsilon Delta'
    site_footer = 'power by atlednolispe'


xadmin.site.register(CommAdminView, GlobalSetting)
