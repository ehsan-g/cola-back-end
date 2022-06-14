from buildings.models import Building
from .serializers import BuildingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BuildingSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import (
    IsAuthenticated,
)

# Create your views here.
class BuildingList(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        products = Building.objects.filter(is_active=True)
        serializer = BuildingSerializer(products, many=True)
        return Response({"products": serializer.data})

