from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from books.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomePageView(TemplateView):

    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Book.GENRE_CHOICES 
        return context

class AboutPageView(TemplateView):

    template_name = 'pages/about.html'

class CartListView(LoginRequiredMixin, ListView):

    model = Book
    template_name = 'account/cart.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        
        user = self.request.user

        return user.profile.cart.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = self.request.user.profile.cart.all()
        total = cart_items.aggregate(
                total_price=Sum('price')
            )['total_price'] or 0
        context['full_price'] = total
        return context