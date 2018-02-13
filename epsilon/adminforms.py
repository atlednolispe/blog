from django import forms


class TagAdminForm(forms.ModelForm):
    status = forms.BooleanField(label='正常', required=False)
    desc = forms.CharField(widget=forms.Textarea, label='简单描述', required=False)
