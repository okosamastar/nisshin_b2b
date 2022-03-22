from django.views.generic import DetailView, ListView

from .models import Category, Facility, Industry, Product, Tag

# Create your views here.


class CategoriesView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(parent_id__isnull=True)


class ProductsView(ListView):
    model = Product

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
        context["current_category"] = Category.objects.get(slug=cat)
        context["tag_list"] = Tag.objects.all()
        context["category_list"] = Category.objects.filter(parent_id__isnull=True)
        return context


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["facility_list"] = Facility.objects.all()
        context["industry_list"] = Industry.objects.all()
        context["category_list"] = Category.objects.filter(parent_id__isnull=True)
        for tag in Tag.objects.all():
            if tag.slug == "dry":
                context["preservation"] = tag
            elif tag.slug == "frozen":
                context["preservation"] = tag
        return context
