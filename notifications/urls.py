from django.urls import path

from notifications import views

app_name = "notifications"

urlpatterns = [
    path(
        "notify/new_borrowing/",
        views.send_new_borrowing_notification_view,
        name="new_borrowing",
    ),
    path(
        "notify/overdue/",
        views.send_overdue_borrowing_notification_view,
        name="overdue_borrowing",
    ),
    path(
        "notify/payment_success/",
        views.send_successful_payment_notification_view,
        name="payment_success",
    ),
]
