from django.shortcuts import render
from django.views.defaults import page_not_found
from django.views.generic import ListView, TemplateView

from products.models import Category


# Create your views here.
class homeView(ListView):
    model = Category
    template_name = "pages/home.html"

    def get_queryset(self):
        return Category.objects.filter(parent_id__isnull=True)


class contactView(TemplateView):
    template_name = "pages/contact.html"


class storeView(TemplateView):
    template_name = "pages/ec.html"


class micstoreView(TemplateView):
    template_name = "pages/micstore.html"


def custom_page_not_found(request):
    return page_not_found(request, None)


def spring_2022(request):
    return render(request, "pages/spring_2022.html")


def health_check(request):
    return render(request, "pages/healthcheck.html")
