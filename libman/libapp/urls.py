from django.conf.urls import url
from .views import create_books

urlpatterns = [
    url(r'add_books/', create_books, name='create_books')
]