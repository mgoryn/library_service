import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestPaymentViews:
    def setup_method(self):
        self.client = APIClient()

    def test_success_payment(self):
        response = self.client.get(reverse("payments:success"))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "Payment successful!"

    def test_cancel_payment(self):
        response = self.client.get(reverse("payments:cancel"))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "Payment was cancelled."
