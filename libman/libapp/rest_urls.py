from django.conf.urls import url
from .rest_views import book_view, BookView, BookDetailView, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('book_api', BookViewSet)

urlpatterns = [
    url(r'view_books/', book_view, name='view_books'),
    url(r'book_view/', BookView.as_view(), name="bookapi_view"),
    url(r'list_view/', BookDetailView.as_view(), name='list_view')
]

urlpatterns += router.urls