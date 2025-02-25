from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("borrowing", "status", "type", "money_to_pay", "session_id")
    search_fields = ("borrowing__user__email", "session_id")
    list_filter = ("status", "type")
