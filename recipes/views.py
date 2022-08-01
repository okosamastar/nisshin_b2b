from braces.views import PrefetchRelatedMixin
from django.db.models import Count
from django.views.generic import DetailView, ListView

from .models import Category, Recipe, RecommendedItem, Tag


# Create your views here.
class HomeView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(show_in_menu=True)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context["latest"] = Recipe.objects.filter(is_new=True).order_by("created")[:8]
        context["recommended"] = RecommendedItem.objects.all()

        return context


class RecipesView(PrefetchRelatedMixin, ListView):
    model = Recipe
    allow_empty = False
    prefetch_related = ["category", "photos"]

    def get_queryset(self):
        cat = self.kwargs["cat"]
        queryset = Recipe.objects.filter(category__slug=cat, is_published=True)
        if "child" in self.kwargs:
            child = self.kwargs["child"]
            queryset = queryset.filter(category__slug=child)
        if "tag" in self.kwargs:
            tag = self.kwargs["tag"]
            queryset = queryset.filter(tag__slug=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(RecipesView, self).get_context_data(**kwargs)
        cat = self.kwargs["cat"]

        current_category = Category.objects.get(slug=cat)
        if current_category.parent:
            current_category = current_category.parent

        context["current_category"] = current_category
        context["subcategories"] = (
            current_category.child.filter(recipe__is_published=True)
            .annotate(Count("recipe"))
            .order_by("the_order")
        )

        recipe_in_category = Recipe.objects.filter(
            category__slug=current_category.slug, is_published=True
        )
        context["all_count"] = recipe_in_category.count()

        # tag_all = Tag.objects.all().order_by("the_order")
        tag_matched = Tag.objects.filter(
            recipe__in=list(recipe_in_category.values_list("id", flat=True))
        ).annotate(Count("recipe"))

        # product_serched = Product.objects.filter(category__slug=cat)
        # only matched in search results
        # tag_matched = Tag.objects.filter(
        #     product__in=list(self.object_list.values_list("id", flat=True))
        # )

        # for tag in tag_all:
        #     if tag in tag_matched:
        #         tag.active = True
        #         tag.count = tag_matched.get(id=tag.pk).recipe__count
        #     else:
        #         tag.active = False
        #         tag.count = 0

        context["tag_list"] = tag_matched

        return context


class RecipeDetail(PrefetchRelatedMixin, DetailView):
    model = Recipe
    allow_empty = False
    prefetch_related = ["category", "tag", "sub_recipe", "related"]

    def get_queryset(self):
        return self.model.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super(RecipeDetail, self).get_context_data(**kwargs)
        return context
