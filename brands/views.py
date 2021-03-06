from braces.views import PrefetchRelatedMixin
from django.http import Http404
from django.template import TemplateDoesNotExist, loader
from django.views.generic import ListView

from products.models import Product


class BrandView(PrefetchRelatedMixin, ListView):
    model = Product
    allow_empty = False
    prefetch_related = ["category", "photos"]

    def get_queryset(self):
        brand = self.kwargs["brand"]
        queryset = Product.objects.filter(
            brand__slug=brand, is_published=True, category__parent_id__isnull=True
        ).order_by("category")
        if "series" in self.kwargs:
            series = self.kwargs["series"]
            queryset = queryset.filter(series__slug=series)
        return queryset

    def get_template_names(self):
        template = ""
        if "series" in self.kwargs:
            template = "brands/%s.html" % self.kwargs["series"]
        elif "brand" in self.kwargs:
            template = "brands/%s.html" % self.kwargs["brand"]

        try:
            loader.get_template(template)
            return template
        except TemplateDoesNotExist:
            raise Http404
