from rest_framework import viewsets

from back.book.models import Book
from back.api.book.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
