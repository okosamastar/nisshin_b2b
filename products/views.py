from django.views.generic import DetailView, ListView

from .models import Category, Facility, Industry, Product

# Create your views here.


class CategoriesView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(parent_id__isnull=True)


class ProductsView(ListView):
    model = Product

    def get_queryset(self):
        cat = self.kwargs["cat"]
        return Product.objects.filter(category__slug=cat)

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        cat = self.kwargs["cat"]
        context["current_category"] = Category.objects.get(slug=cat)
        context["category_list"] = Category.objects.filter(parent_id__isnull=True)
        return context


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["facility_list"] = Facility.objects.all()
        context["industry_list"] = Industry.objects.all()
        context["category_list"] = Category.objects.filter(parent_id__isnull=True)
        return context
