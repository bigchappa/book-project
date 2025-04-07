from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
#from books.models import Book

# Create your models here.
class CustomUser(AbstractUser):
    pass

class UserProfile(models.Model):

    avatar = models.ImageField(upload_to='avatars/', blank=True)
    bio = models.TextField(blank=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    books = models.ManyToManyField('books.Book', blank=True, related_name='profiles')
    cart = models.ManyToManyField(
        'books.Book', 
        blank=True, 
        related_name='profiles_with_cart'
    )