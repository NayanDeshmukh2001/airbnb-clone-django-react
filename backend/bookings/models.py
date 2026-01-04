from django.db import models
from users.models import User
from properties.models import Property


class Availability(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="availability"
    )

    date = models.DateField()
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ("property", "date")

    def __str__(self):
        return f"{self.property.title} - {self.date}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    ]

    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    check_in = models.DateField()
    check_out = models.DateField()
    guests_count = models.PositiveIntegerField()

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property.title} ({self.status})"
