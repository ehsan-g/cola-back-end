from buildings.models import Building
from .serializers import BuildingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BuildingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import (
    IsAuthenticated,
)

# Create your views here.
class BuildingList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.company == 1:
            buildings = Building.objects.filter(company=1).filter(is_active=True)

        if user.company == 2:
            buildings = Building.objects.filter(company=2).filter(is_active=True)

        if user.company == 0 and user.is_superuser:
            buildings = Building.objects.filter(is_active=True)

        serializer = BuildingSerializer(buildings, many=True)
        return Response({"buildings": serializer.data})
