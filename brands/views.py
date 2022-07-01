from django.http import Http404
from django.template import TemplateDoesNotExist, loader
from django.views.generic import TemplateView


class BrandView(TemplateView):
    def get_template_names(self):
        template = "brands/%s.html" % self.kwargs["brand"]
        try:
            loader.get_template(template)
            return template
        except TemplateDoesNotExist:
            raise Http404
