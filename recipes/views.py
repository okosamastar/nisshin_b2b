from braces.views import PrefetchRelatedMixin

# from django.db.models import Count
from django.views.generic import DetailView

from .models import Recipe


# Create your views here.
class RecipeDetail(PrefetchRelatedMixin, DetailView):
    model = Recipe
    allow_empty = False
    prefetch_related = ["category", "tag", "sub_recipe", "related"]

    def get_queryset(self):
        return self.model.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super(RecipeDetail, self).get_context_data(**kwargs)
        return context
