from django.views.generic import TemplateView

from .forms import CommentForm


class CommentView(TemplateView):
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.target = request.POST.get('target')
            comment.save()
            succeed = True
        else:
            succeed = False

        extra_context = {
            'succeed': succeed,
            'form': comment_form,
        }

        context = self.get_context_data(**kwargs)
        context.update(extra_context)
        return self.render_to_response(context)


