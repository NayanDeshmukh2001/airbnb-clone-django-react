from datetime import timedelta
from bookings.models import Availability
from .models import Property


def daterange(start_date, end_date):
    current = start_date
    while current < end_date:
        yield current
        current += timedelta(days=1)


def search_properties(city, check_in, check_out, guests):
    queryset = Property.objects.filter(
        city__icontains=city,
        max_guests__gte=guests,
        is_active=True
    )

    available_properties = []

    for prop in queryset:
        blocked = Availability.objects.filter(
            property=prop,
            date__gte=check_in,
            date__lt=check_out,
            is_available=False
        ).exists()

        if not blocked:
            available_properties.append(prop)

    return available_properties
