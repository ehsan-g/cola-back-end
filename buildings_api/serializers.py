from rest_framework import serializers
from buildings.models import (
    Building,
    BuildingImage,
    Address,
    Floor,
    Room,
    MyEvent,
    FloorLayout,
)


class FloorLayOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorLayout
        fields = "__all__"


class BuildingSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)
    address = serializers.SerializerMethodField(read_only=True)
    floors = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Building
        fields = (
            "id",
            "building_name",
            "description",
            "company",
            "image",
            "address",
            "floors",
        )

    def get_image(self, obj):
        image = obj.building_image
        serializer = BuildingImageSerializer(image, many=False)
        return serializer.data

    def get_address(self, obj):
        address = obj.building_address
        serializer = AddressSerializer(address, many=False)
        return serializer.data

    def get_floors(self, obj):
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
    rooms = serializers.SerializerMethodField(read_only=True)
    layout = serializers.SerializerMethodField(read_only=True)

    def get_rooms(self, obj):
        room = obj.floor_rooms
        serializer = RoomSerializer(room, many=True)
        return serializer.data

    def get_layout(self, obj):
        layout = obj.layout
        serializer = FloorLayOutSerializer(layout, many=False)
        return serializer.data

    class Meta:
        model = Floor
        fields = "__all__"


class MyEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyEvent
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    events_room = serializers.SerializerMethodField(read_only=True)

    def get_events_room(self, obj):
        events = obj.events_room
        serializer = MyEventSerializer(events, many=True)
        return serializer.data

    class Meta:
        model = Room
        fields = "__all__"
