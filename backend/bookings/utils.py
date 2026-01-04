from datetime import date, timedelta
from django.db import transaction
from .models import Booking, Availability


def daterange(start_date, end_date):
    current = start_date
    while current < end_date:
        yield current
        current += timedelta(days=1)


@transaction.atomic
def cancel_booking(booking: Booking):
    """
    Cancels a booking and releases availability.
    """
    if booking.status == 'cancelled':
        return

    booking.status = 'cancelled'
    booking.save()

    for day in daterange(booking.check_in, booking.check_out):
        Availability.objects.filter(
            property=booking.property,
            date=day
        ).update(is_available=True)


def complete_bookings():
    """
    Marks bookings as completed after checkout date.
    Intended for cron / scheduled task.
    """
    today = date.today()

    bookings = Booking.objects.filter(
        status='confirmed',
        check_out__lt=today
    )

    bookings.update(status='completed')
