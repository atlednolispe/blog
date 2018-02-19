from django.shortcuts import redirect
from django.views.generic import TemplateView

from .forms import CommentForm
from .models import Comment


class CommentShowMixin:
    def get_comments(self):
        target = self.request.path
        comments = Comment.objects.filter(target=target).order_by('-id')
        return comments

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(),
            'comment_list': self.get_comments(),
        })
        return super().get_context_data(**kwargs)


class CommentView(TemplateView):
    template_name = 'comment/result.html'
    http_method_names = ('post',)

    def post(self, request, *args, **kwargs):
        # TODO(altednolispe) To delete some garbage code.
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.target = target
            comment.save()
            succeed = True  #
            return redirect(target)
        else:
            succeed = False

        extra_context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target,  #
        }

        context = self.get_context_data(**kwargs)
        context.update(extra_context)
        return self.render_to_response(context)
