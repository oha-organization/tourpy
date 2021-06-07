from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView, ListView
from .models import Page
from .models import Slide
from .models import TourCategory,Tour


class HomePageView(ListView): #birden fazla model gönderim örneği var. 
    model=Slide
    context_object_name = 'Slides'
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        ctx = super(HomePageView, self).get_context_data(**kwargs)
        ctx['TourCategory'] = TourCategory.objects.order_by('title')
        return ctx


class PageDetailView(DetailView):
    model = Page
    template_name = 'page_detail.html'

class CategoryDetailView(DetailView):
    model = TourCategory
    template_name = 'category_detail.html'

class TourDetailView(DetailView):
    model = Tour
    template_name = 'tour_detail.html'

