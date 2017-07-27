from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.
class BookManager(models.Manager):
    def AddBook(self, form_data, user):
        book = Book.objects.create(
            title = form_data['title'],
            author = form_data['author'],
            review = form_data['review'],
            rating = form_data['rating'],
            user = user,
        )
        return book


class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='books')
    review = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()
