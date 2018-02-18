from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="内容", widget=forms.widgets.Textarea(attrs={'rows': 6, 'cols': 80}))

    def clean_content(self):
        content = self.cleaned_data.get('content')

        if len(content) < 10:
            raise forms.ValidationError('soooooo short')
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
