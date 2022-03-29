from django.db.models import Count
from django.views.generic import DetailView, ListView

from .models import Category, Facility, Industry, Product, Tag

# Create your views here.


class CategoriesView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(parent_id__isnull=True)


class ProductsView(ListView):
    model = Product
    allow_empty = False

    def get_queryset(self):
        cat = self.kwargs["cat"]
        list = Product.objects.filter(category__slug=cat)
        if "child" in self.kwargs:
            child = self.kwargs["child"]
            list = list.filter(category__slug=child)
        if "tag" in self.kwargs:
            tag = self.kwargs["tag"]
            list = list.filter(tag__slug=tag)
        return list

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        cat = self.kwargs["cat"]

        current_category = Category.objects.get(slug=cat)
        if current_category.parent:
            current_category = current_category.parent

        context["current_category"] = current_category
        context["subcategories"] = (
            current_category.child.all()
            .annotate(Count("product"))
            .order_by("the_order")
        )
        context["category_list"] = Category.objects.filter(parent_id__isnull=True)

        product_in_category = Product.objects.filter(
            category__slug=current_category.slug
        )
        context["all_count"] = product_in_category.count()

        tag_all = Tag.objects.all().order_by("the_order")
        tag_matched = Tag.objects.filter(
            product__in=list(product_in_category.values_list("id", flat=True))
        ).annotate(Count("product"))

        # product_serched = Product.objects.filter(category__slug=cat)
        # only matched in search results
        # tag_matched = Tag.objects.filter(
        #     product__in=list(self.object_list.values_list("id", flat=True))
        # )

        for tag in tag_all:
            if tag in tag_matched:
                tag.active = True
                tag.count = tag_matched.get(id=tag.pk).product__count
            else:
                tag.active = False
                tag.count = 0

        context["tag_list"] = tag_all

        return context


class ProductDetail(DetailView):
    model = Product
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        products = context.get("object")

        context["current_category"] = products.category.get(parent_id__isnull=True)
        context["facility_list"] = Facility.objects.all()
        context["industry_list"] = Industry.objects.all()
        context["category_list"] = Category.objects.filter(parent_id__isnull=True)

        return context
