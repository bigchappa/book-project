from django.contrib import admin
from . import models

# Register your models here.

class ReviewInLine(admin.TabularInline):

    model = models.Review

class BookAdmin(admin.ModelAdmin):

    inlines = [
        ReviewInLine,
    ]

    list_display = ['title', 'author', 'price']

admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Like)