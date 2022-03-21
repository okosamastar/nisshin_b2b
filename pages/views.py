from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class homeView(TemplateView):
    template_name = "pages/home.html"


class contactView(TemplateView):
    template_name = "pages/contact.html"


class storestView(TemplateView):
    template_name = "pages/ec.html"


def spring_2022(request):
    return render(request, "pages/spring_2022.html")