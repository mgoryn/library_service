from django.db import models

from borrowings.models import Borrowing


class Payment(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
    )
    TYPE_CHOICES = (
        ("PAYMENT", "Payment"),
        ("FINE", "Fine"),
    )
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="PAYMENT")
    session_url = models.URLField()
    session_id = models.CharField(max_length=100)
    money_to_pay = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Payment {self.id} for Borrowing {self.borrowing.id}"
