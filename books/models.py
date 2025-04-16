from django.contrib.auth import get_user_model
from django.db import models
import uuid

class Author(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    photo = models.ImageField(upload_to='covers/', blank=True)
    name = models.CharField(max_length=120)
    bio = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:

        permissions = [
            ('add_author_status', 'Can add author'),
        ]

class Book(models.Model):   

    GENRE_CHOICES = [
        ('FAN', 'Фантастика'),
        ('DET', 'Детектив'),
        ('ROM', 'Роман'),
        ('HOR', 'Ужасы'),
        ('HIS', 'Исторический'),
        ('BIO', 'Биография'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)
    genre = models.CharField(
        max_length=3,
        choices=GENRE_CHOICES,
        default='FAN'
    )

    class Meta:

        permissions = [
            ('special_status', 'Can read all books'),
            ('add_book_status', 'Can add book'),
        ]

    

    def __str__(self):

        return self.title 

    
class Review(models.Model):

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=478)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):

        return self.review
    
class Like(models.Model):

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='likes',
    )