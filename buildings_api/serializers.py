from rest_framework import serializers
from buildings.models import Building, BuildingImage, Address, Room, Floor


class BuildingSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)
    address = serializers.SerializerMethodField(read_only=True)
    floor = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Building
        fields = (
            "id",
            "building_name",
            "description",
            "company",
            "image",
            "address",
            "floor",
        )

    def get_image(self, obj):
        image = obj.building_image
        serializer = BuildingImageSerializer(image, many=False)
        return serializer.data

    def get_address(self, obj):
        address = obj.building_address
        serializer = AddressSerializer(address, many=False)
        return serializer.data

    def get_floor(self, obj):
        floor = obj.building_floor
        serializer = FloorSerializer(floor, many=True)
        return serializer.data


class BuildingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingImage
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class FloorSerializer(serializers.ModelSerializer):
    def get_room(self, obj):
        room = obj.floor_room
        serializer = RoomSerializer(room, many=True)
        return serializer.data

    class Meta:
        model = Floor
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
