from django.db import models
from django.conf import settings
from bookings.models import Booking
from properties.models import Property

User = settings.AUTH_USER_MODEL


class Review(models.Model):
    """
    Review left by a guest after completing a stay.
    """

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name='review'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    rating = models.PositiveSmallIntegerField(
        help_text="Rating from 1 to 5"
    )
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property.title} - {self.rating}/5 by {self.user}"
