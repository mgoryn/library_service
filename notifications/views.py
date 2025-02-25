from django.http import JsonResponse

from notifications.tasks import (
    send_new_borrowing_notification,
    send_overdue_borrowing_notification,
    send_successful_payment_notification,
)


def send_new_borrowing_notification_view(request):
    chat_id = "ADMIN_CHAT_ID"  # Test chat_id
    book_title = "Test Book"
    user_name = "Test User"

    send_new_borrowing_notification.delay(chat_id, book_title, user_name)

    return JsonResponse({"message": "New borrowing notification sent!"})


def send_overdue_borrowing_notification_view(request):
    chat_id = "ADMIN_CHAT_ID"  # Test chat_id
    book_title = "Test Overdue Book"
    user_name = "Test User"

    send_overdue_borrowing_notification.delay(chat_id, book_title, user_name)

    return JsonResponse({"message": "Overdue borrowing notification sent!"})


def send_successful_payment_notification_view(request):
    chat_id = "ADMIN_CHAT_ID"  # Test chat_id
    amount = 25.99
    user_name = "Test User"

    send_successful_payment_notification.delay(chat_id, amount, user_name)

    return JsonResponse({"message": "Successful payment notification sent!"})
