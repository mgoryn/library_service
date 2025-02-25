import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from books.models import Book
from borrowings.models import Borrowing

User = get_user_model()


@pytest.mark.django_db
class TestBorrowingViewSet:
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com", password="password123"
        )
        self.book = Book.objects.create(
            title="Book 1",
            author="Author 1",
            inventory=5,
            daily_fee="1.50",
            cover="HARD",
        )

    def test_create_borrowing(self):
        payload = {
            "book": self.book.id,
            "borrow_date": "2025-02-25",
            "expected_return_date": "2025-03-01",
            "user": self.user.id,
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse("borrowings:borrowing-list"), payload)
        assert response.status_code == status.HTTP_201_CREATED
        assert Borrowing.objects.count() == 1

    def test_list_borrowings(self):
        Borrowing.objects.create(
            book=self.book,
            borrow_date="2025-02-20",
            expected_return_date="2025-02-27",
            user=self.user,
        )
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("borrowings:borrowing-list"))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
