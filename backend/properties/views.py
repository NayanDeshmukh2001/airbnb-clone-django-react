from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Property
from .serializers import PropertySerializer


class HostPropertyListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        properties = Property.objects.filter(user=request.user)
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView

from .models import Property
from .serializers import PropertySerializer


class PropertyCreateAPIView(CreateAPIView):
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}
