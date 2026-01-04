from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            "id",
            "title",
            "description",
            "property_type",
            "city",
            "country",
            "address",
            "price_per_night",
            "max_guests",
            "bedrooms",
            "bathrooms",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        return super().create(validated_data)
