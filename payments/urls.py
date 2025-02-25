from django.urls import path

from payments import views

app_name = "payments"

urlpatterns = [
    path("success/", views.success_payment, name="success_payment"),
    path("cancel/", views.cancel_payment, name="cancel_payment"),
]
