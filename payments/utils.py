import stripe
from django.conf import settings

from payments.models import Payment

stripe.api_key = settings.STRIPE_API_KEY


def create_stripe_payment_session(borrowing_id, amount):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": f"Borrowing {borrowing_id}",
                    },
                    "unit_amount": int(amount * 100),
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="http://localhost:8000/success/",
        cancel_url="http://localhost:8000/cancel/",
    )
    payment = Payment.objects.create(
        borrowing_id=borrowing_id,
        session_url=session.url,
        session_id=session.id,
        money_to_pay=amount,
    )
    return session.url
