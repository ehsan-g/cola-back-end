from rest_framework import serializers
from buildings.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ("id", "building_name", "description", "company")
