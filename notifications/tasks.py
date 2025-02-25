from celery import shared_task

from notifications.utils import send_telegram_message


@shared_task
def send_new_borrowing_notification(chat_id, book_title, user_name):
    """Task for sending a notification about a new loan."""
    message = f"New borrowing created:\nBook: {book_title}\nUser: {user_name}"
    send_telegram_message(chat_id, message)


@shared_task
def send_overdue_borrowing_notification(chat_id, book_title, user_name):
    """Task for sending a notification about an overdue loan."""
    message = f"Overdue borrowing:\nBook: {book_title}\nUser: {user_name}"
    send_telegram_message(chat_id, message)


@shared_task
def send_successful_payment_notification(chat_id, amount, user_name):
    """A task for sending a notification about a successful payment."""
    message = f"Payment successful:\nAmount: ${amount}\nUser: {user_name}"
    send_telegram_message(chat_id, message)
