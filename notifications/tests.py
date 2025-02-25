from unittest.mock import patch

from notifications.tasks import send_telegram_message


def test_send_telegram_message():
    with patch("notifications.tasks.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        send_telegram_message("Test message")
        mock_post.assert_called_once()
