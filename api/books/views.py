from rest_framework import viewsets, mixins

from api.books.models import Book
from api.books.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
