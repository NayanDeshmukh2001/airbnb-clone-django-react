from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from bookings.models import Booking

class HostBookingListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        host = request.user

        bookings = Booking.objects.filter(
            property__host=host
        ).select_related("property", "guest")

        data = []
        for booking in bookings:
            data.append({
                "id": booking.id,
                "property": booking.property.title,
                "guest": booking.guest.username,
                "check_in": booking.check_in,
                "check_out": booking.check_out,
                "guests": booking.guests_count,
                "total_price": booking.total_price,
                "status": booking.status,
            })

        return Response(data)
