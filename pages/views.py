from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import Book

# Create your views here.
class HomePageView(TemplateView):

    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Book.GENRE_CHOICES 
        return context

class AboutPageView(TemplateView):

    template_name = 'pages/about.html'