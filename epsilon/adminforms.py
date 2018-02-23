from ckeditor.fields import CKEditorWidget
from dal import autocomplete
from django import forms

from .models import Category, Tag


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'), label='内容')
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),  # constraint
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )
    tags = forms.ModelMultipleChoiceField(  # ManyToMany
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )


class TagAdminForm(forms.ModelForm):
    status = forms.BooleanField(label='正常', required=False)
    desc = forms.CharField(widget=forms.Textarea, label='简单描述', required=False)
