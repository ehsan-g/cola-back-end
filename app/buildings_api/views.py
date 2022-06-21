from buildings.models import Building, Floor
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
from django.db.models import Q
from rest_framework.decorators import api_view
from buildings.models import (
    Building,
)
from django.http import HttpResponse
import json

# for admin and change_form.html
@api_view(["GET"])
def get_building_floor(request):
    id = request.GET.get("id", "")
    result = list(Floor.objects.filter(building_id=int(id)).values("id", "title"))
    return HttpResponse(json.dumps(result), content_type="application/json")


# Create your views here.
class BuildingList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.company == 1:
            buildings = Building.objects.filter(Q(company=1) | Q(company=3)).filter(
                is_active=True
            )

        if user.company == 2:
            buildings = Building.objects.filter(Q(company=2) | Q(company=3)).filter(
                is_active=True
            )

        if user.company == 0 and user.is_superuser:
            buildings = Building.objects.filter(is_active=True)

        serializer = BuildingSerializer(buildings, many=True)
        return Response({"buildings": serializer.data})
