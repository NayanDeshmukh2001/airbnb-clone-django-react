from django.db.models import Sum, Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from properties.models import Property
from bookings.models import Booking

class HostDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        host = request.user

        properties = Property.objects.filter(host=host).annotate(
            total_bookings=Count("bookings"),
            total_earnings=Sum("bookings__total_price")
        )

        property_data = []
        for prop in properties:
            property_data.append({
                "id": prop.id,
                "title": prop.title,
                "city": prop.city,
                "price_per_night": prop.price_per_night,
                "total_bookings": prop.total_bookings,
                "total_earnings": prop.total_earnings or 0,
            })

        recent_bookings = Booking.objects.filter(
            property__host=host
        ).order_by("-created_at")[:5]

        bookings_data = [
            {
                "property": booking.property.title,
                "guest": booking.guest.username,
                "status": booking.status,
                "total_price": booking.total_price,
                "check_in": booking.check_in,
                "check_out": booking.check_out,
            }
            for booking in recent_bookings
        ]

        return Response({
            "host": host.username,
            "properties": property_data,
            "recent_bookings": bookings_data,
        })
