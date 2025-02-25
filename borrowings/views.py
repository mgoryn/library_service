from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from borrowings.models import Borrowing
from borrowings.serializers import BorrowingSerializer
from notifications.tasks import send_new_borrowing_notification


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")
        is_active = self.request.query_params.get("is_active")

        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if is_active is not None:
            if is_active.lower() == "true":
                queryset = queryset.filter(actual_return_date__isnull=True)
            elif is_active.lower() == "false":
                queryset = queryset.filter(actual_return_date__isnull=False)

        return queryset

    @action(detail=True, methods=["post"])
    def return_borrowing(self, request, pk=None):
        borrowing = self.get_object()
        if borrowing.actual_return_date:
            return Response({"detail": "This borrowing is already returned."}, status=status.HTTP_400_BAD_REQUEST)

        borrowing.actual_return_date = request.data.get("actual_return_date")
        borrowing.book.inventory += 1
        borrowing.book.save()
        borrowing.save()
        return Response({"detail": "Book returned successfully."})


def create_borrowing(request):
    chat_id = "ADMIN_CHAT_ID"  # Change to real CHAT-ID
    book_title = "Book Title"
    user_name = "User Name"
    send_new_borrowing_notification.delay(chat_id, book_title, user_name)
