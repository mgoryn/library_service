import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from books.models import Book


@pytest.mark.django_db
class TestBookViewSet:
    def setup_method(self):
        self.client = APIClient()

    def test_create_book(self):
        payload = {
            "title": "Test Book",
            "author": "Author Name",
            "inventory": 5,
            "daily_fee": "1.50",
            "cover": "HARD",
        }
        response = self.client.post(reverse("books:book-list"), payload)
        assert response.status_code == status.HTTP_201_CREATED
        assert Book.objects.count() == 1

    def test_list_books(self):
        Book.objects.create(
            title="Book 1",
            author="Author 1",
            inventory=3,
            daily_fee="2.00",
            cover="SOFT",
        )
        response = self.client.get(reverse("books:book-list"))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_retrieve_book(self):
        book = Book.objects.create(
            title="Book 2",
            author="Author 2",
            inventory=4,
            daily_fee="3.00",
            cover="HARD",
        )
        url = reverse("books:book-detail", args=[book.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "Book 2"

    def test_update_book(self):
        book = Book.objects.create(
            title="Book 3",
            author="Author 3",
            inventory=2,
            daily_fee="4.00",
            cover="SOFT",
        )
        url = reverse("books:book-detail", args=[book.id])
        payload = {"title": "Updated Book"}
        response = self.client.patch(url, payload)
        assert response.status_code == status.HTTP_200_OK
        book.refresh_from_db()
        assert book.title == "Updated Book"

    def test_delete_book(self):
        book = Book.objects.create(
            title="Book 4",
            author="Author 4",
            inventory=1,
            daily_fee="5.00",
            cover="HARD",
        )
        url = reverse("books:book-detail", args=[book.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Book.objects.filter(id=book.id).exists()
