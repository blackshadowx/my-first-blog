from django.shortcuts import render
from django.views.generic import TemplateView
from . import templates

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
class AboutPageView(TemplateView):
    template_name = "about.html"
class SinglePageView(TemplateView):
    template_name = "single.html"
class ContactPageView(TemplateView):
    template_name = "contact.html"
