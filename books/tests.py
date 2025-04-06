from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from . import models

class BookTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@mail.ru',
            password='passwordtest',
        )

        self.book = models.Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )

        self.review = models.Review.objects.create(
            author=self.user,
            book=self.book,
            review='good book)',
        )

    def test_book_listing(self):

        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view(self):

        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):

        response = self.client.get(reverse('book_detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response, 'good book)')
        