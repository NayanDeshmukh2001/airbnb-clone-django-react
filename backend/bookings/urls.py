from django.urls import path
from .views import HostBookingListAPIView

urlpatterns = [
    path("host/", HostBookingListAPIView.as_view(), name="host-bookings"),
]
