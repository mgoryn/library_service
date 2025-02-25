from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "inventory", "daily_fee", "cover")
    search_fields = ("title", "author")
    list_filter = ("cover",)
    ordering = ("title",)
