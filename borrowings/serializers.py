from rest_framework import serializers

from borrowings.models import Borrowing


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ["id", "borrow_date", "expected_return_date", "actual_return_date", "book", "user"]
        read_only_fields = ["borrow_date", "actual_return_date", "user"]

    def validate(self, data):
        if data["expected_return_date"] <= data["borrow_date"]:
            raise serializers.ValidationError("Expected return date must be after borrow date.")
        return data

    def create(self, validated_data):
        book = validated_data["book"]
        if book.inventory < 1:
            raise serializers.ValidationError("Book is out of stock.")
        book.inventory -= 1
        book.save()
        borrowing = Borrowing.objects.create(**validated_data)
        return borrowing
