from datetime import timedelta
from django.db import transaction
from django.utils import timezone

from .models import Availability, Booking
from properties.models import Property


def daterange(start_date, end_date):
    """
    Generates dates from start_date to end_date (excluding end_date).
    """
    current = start_date
    while current < end_date:
        yield current
        current += timedelta(days=1)


def check_availability(property: Property, check_in, check_out) -> bool:
    """
    Returns True if all dates are available for the property.
    """
    unavailable_dates = Availability.objects.filter(
        property=property,
        date__gte=check_in,
        date__lt=check_out,
        is_available=False
    ).exists()

    return not unavailable_dates


def calculate_total_price(property: Property, check_in, check_out):
    """
    Calculates total price based on number of nights.
    """
    nights = (check_out - check_in).days
    return nights * property.price_per_night


@transaction.atomic
def create_booking(user, property: Property, check_in, check_out):
    """
    Creates a booking and blocks availability atomically.
    """

    if check_in >= check_out:
        raise ValueError("Check-out date must be after check-in date")

    if not check_availability(property, check_in, check_out):
        raise ValueError("Selected dates are not available")

    total_price = calculate_total_price(property, check_in, check_out)

    booking = Booking.objects.create(
        user=user,
        property=property,
        check_in=check_in,
        check_out=check_out,
        total_price=total_price,
        status='pending'
    )

    # Block dates
    for date in daterange(check_in, check_out):
        Availability.objects.update_or_create(
            property=property,
            date=date,
            defaults={'is_available': False}
        )

    return booking
