import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from payments.models import Borrowing, Payment

stripe.api_key = settings.STRIPE_API_KEY


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    endpoint_secret = "endpoint-secret"

    event = None
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        return JsonResponse({"message": "Invalid payload"}, status=400)
    except stripe.error.SignatureVerificationError as e:
        return JsonResponse({"message": "Invalid signature"}, status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        payment_id = session["id"]
        payment = Payment.objects.get(session_id=payment_id)
        payment.status = "PAID"
        payment.save()

    return JsonResponse({"status": "success"}, status=200)


def success_payment(request):
    borrowing_id = request.GET.get("borrow_id")

    try:
        borrowing = Borrowing.objects.get(id=borrowing_id)
    except Borrowing.DoesNotExist:
        return JsonResponse({"message": "Borrowing not found."}, status=404)

    payment = Payment.objects.filter(borrowing=borrowing, status="PENDING").first()
    if payment:
        payment.status = "PAID"
        payment.save()

    borrowing.is_active = False
    borrowing.save()

    return JsonResponse({"message": "Payment successful!"})


def cancel_payment(request):
    borrowing_id = request.GET.get("borrow_id")

    try:
        borrowing = Borrowing.objects.get(id=borrowing_id)
    except Borrowing.DoesNotExist:
        return JsonResponse({"message": "Borrowing not found."}, status=404)

    payment = Payment.objects.filter(borrowing=borrowing, status="PENDING").first()
    if payment:
        payment.status = "CANCELLED"
        payment.save()

    borrowing.is_active = True
    borrowing.save()

    return JsonResponse({"message": "Payment was cancelled."})
