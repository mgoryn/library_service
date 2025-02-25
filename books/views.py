from rest_framework import viewsets

from books.models import Book
from books.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().prefetch_related()
    serializer_class = BookSerializer
