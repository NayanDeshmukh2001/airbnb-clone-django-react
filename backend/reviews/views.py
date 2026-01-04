from rest_framework import views, status, permissions
from rest_framework.response import Response

from bookings.models import Booking
from .models import Review
from .serializers import ReviewSerializer


class CreateReviewView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        booking_id = request.data.get('booking')
        rating = request.data.get('rating')
        comment = request.data.get('comment', '')

        try:
            booking = Booking.objects.get(
                id=booking_id,
                user=request.user,
                status='completed'
            )

            review = Review.objects.create(
                booking=booking,
                user=request.user,
                property=booking.property,
                rating=rating,
                comment=comment
            )

        except Booking.DoesNotExist:
            return Response(
                {'error': 'Booking not completed or invalid'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
