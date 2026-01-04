from rest_framework import views, status, permissions
from rest_framework.response import Response

from bookings.models import Booking
from .models import Payment
from .serializers import PaymentSerializer


class CreatePaymentView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        booking_id = request.data.get('booking')
        payment_method = request.data.get('payment_method')

        try:
            booking = Booking.objects.get(id=booking_id, user=request.user)

            payment = Payment.objects.create(
                booking=booking,
                amount=booking.total_price,
                payment_method=payment_method,
                status='successful',
                transaction_id='TXN123456'
            )

            booking.status = 'confirmed'
            booking.save()

        except Booking.DoesNotExist:
            return Response(
                {'error': 'Invalid booking'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
