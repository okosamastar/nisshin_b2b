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
        queryset = Product.objects.filter(brand__slug=brand, is_published=True)
        return queryset

    def get_template_names(self):
        template = "brands/%s.html" % self.kwargs["brand"]
        try:
            loader.get_template(template)
            return template
        except TemplateDoesNotExist:
            raise Http404
