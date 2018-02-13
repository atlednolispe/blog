from django import forms


class TagAdminForm(forms.ModelForm):
    status = forms.BooleanField(label='正常', required=False)
    desc = forms.CharField(widget=forms.Textarea, label='简单描述', required=False)

    def clean_status(self):  # 对form传入对status数据转换为models需要的数据
        if self.cleaned_data['status']:
            return 1
        else:
            return 2
