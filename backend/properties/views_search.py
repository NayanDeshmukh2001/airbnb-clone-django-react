from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .search import search_properties
from .serializers import PropertySerializer


class PropertySearchAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        city = request.GET.get("city", "")
        check_in = request.GET.get("check_in")
        check_out = request.GET.get("check_out")
        guests = int(request.GET.get("guests", 1))

        properties = search_properties(
            city=city,
            check_in=check_in,
            check_out=check_out,
            guests=guests
        )

        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
