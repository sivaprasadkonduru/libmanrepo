from django.conf.urls import url
from .views import create_books, add_book, get_books

urlpatterns = [
    url(r'add_books/', create_books, name='create_books'),
    url(r'books_form/', add_book, name='add_book'),
    url(r'all_books', get_books, name='get_books')
]