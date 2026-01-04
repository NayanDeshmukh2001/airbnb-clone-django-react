from django.urls import path
from .views import HostPropertyListAPIView, PropertyCreateAPIView

urlpatterns = [
    path("host/", HostPropertyListAPIView.as_view(), name="host-properties"),
    path("", PropertyCreateAPIView.as_view(), name="property-create"),
]
