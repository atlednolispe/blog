from dal import autocomplete

from epsilon.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:  # is_authenticated from method to attribute by property
            return Category.objects.none()

        qs = Category.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Tag.objects.none()

        qs = Tag.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)
        return qs
