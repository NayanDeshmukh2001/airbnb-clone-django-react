from django.db import models
from users.models import User


class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ("apartment", "Apartment"),
        ("house", "House"),
        ("villa", "Villa"),
        ("hotel", "Hotel"),
    ]

    # Host / Owner
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="properties"
    )

    # Basic info
    title = models.CharField(max_length=255)
    description = models.TextField()
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES
    )

    # Location
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField()

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    # Capacity (⚠ defaults added to avoid migration issues)
    max_guests = models.PositiveIntegerField(default=1)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)

    # Pricing
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    cleaning_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    service_fee_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=10
    )

    # Status
    is_active = models.BooleanField(default=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(upload_to="property_images/")
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.property.title}"
