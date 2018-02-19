from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    # content = forms.CharField(label="内容", widget=forms.widgets.Textarea(attrs={'rows': 6, 'cols': 80}))
    nickname = forms.CharField(
        required=False,
        label='昵称',
        max_length=50,
        widget=forms.widgets.TextInput(),
        empty_value='匿名',
    )

    email = forms.EmailField(
        label='邮箱',
        max_length=50,
        widget=forms.widgets.EmailInput()
    )

    website = forms.URLField(
        label='网站',
        max_length=100,
        widget=forms.widgets.URLInput()
    )

    content = forms.CharField(
        label="内容",
        widget=forms.widgets.Textarea(attrs={'rows': 6, 'cols': 80}),
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')

        if len(content) < 10:
            raise forms.ValidationError('soooooo short')
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
