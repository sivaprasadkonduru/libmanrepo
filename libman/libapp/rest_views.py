from rest_framework import views, viewsets
from rest_framework.generics import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from.serializers import BookSerializer


@api_view(['GET', 'POST'])
def book_view(request):
    if request.method == 'POST':
        return Response({'message': 'Data posted successfully', 'data': request.data})
    return Response({'name': 'Python', 'year': 1990, 'author': 'GuidoVan Rossum'})


class BookView(APIView):

    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)


class BookDetailView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
