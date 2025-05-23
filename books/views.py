from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView
from . import models
from . import forms

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):

    model = models.Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = models.Book.GENRE_CHOICES 
        return context

class AddBookToUser(View):

    def post(self, request, *args, **kwargs):

        book_id = request.POST.get('book_id')
        book = get_object_or_404(
            models.Book,
            pk=book_id,         
        )
        request.user.profile.books.add(book)
        return redirect(request.META.get('HTTP_REFERER', 'book_list'))


class BookDetailView(LoginRequiredMixin, DetailView):

    model = models.Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    #permission_required = 'books.special_status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.ReviewAddForm()
        context['user'] = self.request.user

        return context

    def post(self, request, *args, **kwargs):

        book = self.get_object()

        form = forms.ReviewAddForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.author = request.user
            review.book = book
            review.save()

        return redirect(request.META.get('HTTP_REFERER', 'book_list'), pk=book.pk)
    
class SearchResultView(LoginRequiredMixin, ListView):

    model = models.Book
    context_object_name = 'books'
    template_name = 'books/search_result.html'
    
    def get_queryset(self):
        
        query = self.request.GET.get('q')
        genre = self.request.GET.get('genre')

        if query and genre:

            return models.Book.objects.filter(
                Q(title__icontains=query)|
                Q(author__icontains=query)&
                Q(genre=genre)
            )

        elif genre:

            return models.Book.objects.filter(
                Q(genre=genre)
            )
        
        if query:
            return models.Book.objects.filter(
                    Q(title__icontains=query)|
                    Q(author__icontains=query)
            )
        

    
class AddBookView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    model = models.Book
    fields = '__all__'
    template_name = 'books/add_book.html'
    permission_required = 'books.add_book_status'

    def get_success_url(self):
        
        return reverse('book_detail', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        return self.request.user.is_superuser

class DeleteBookView(LoginRequiredMixin, DeleteView):

    model = models.Book
    success_url = reverse_lazy('book_list')

    def test_func(self):
        return self.request.user.is_superuser
    
class DeleteReviewView(LoginRequiredMixin, DeleteView):

    model = models.Review
    
    def get_success_url(self):
        
        return reverse('book_detail', kwargs={'pk': self.kwargs['book_pk']})
    
class AddLikeView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        review_id = request.POST.get('review_id')
        review = models.Review.objects.get(pk=review_id)

        like, created = models.Like.objects.get_or_create(
            user=request.user,
            review=review,
        )
        
        if not created:

            like.delete()

        return redirect('book_detail', pk=self.kwargs['pk'])
    
class AddBookToCart(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        book_id = request.POST.get('book_id')
        book = get_object_or_404(
            models.Book,
            pk=book_id
        )
        request.user.profile.cart.add(book)
        return redirect(request.META.get('HTTP_REFERER', 'book_detail'), pk=book_id)
    

class AddNewAuthor(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    model = models.Author
    fields = "__all__"
    template_name = 'books/author_creation.html'
    permission_required = 'books.add_author_status'

    def get_success_url(self):
        
        return reverse('author-detail', kwargs={'pk': self.object.pk})
    

class AuthorDetailView(LoginRequiredMixin, DetailView):

    model = models.Author
    template_name = 'books/author-detail.html'
    context_object_name = 'author'
