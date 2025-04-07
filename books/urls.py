from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('search/', views.SearchResultView.as_view(), name='search'),
    path('add-book/', views.AddBookView.as_view(), name='add'),
    path('<uuid:pk>/delete-book/', views.DeleteBookView.as_view(), name='book_delete'),
    path('<uuid:book_pk>/<int:pk>/delete-review/', views.DeleteReviewView.as_view(), name='review_delete'),
    path('<uuid:pk>/like/', views.AddLikeView.as_view(), name='like'),
    path('add-book-to-profile/', views.AddBookToUser.as_view(), name='add-book-to-user')
]