from rest_framework import serializers
from buildings.models import (
    MyEvent,
)
from users_api.serializers import UserSerializer


class MyEventSerializer(serializers.ModelSerializer):
    attendees = serializers.SerializerMethodField(read_only=True)

    def get_attendees(self, obj):
        attendees = obj.attendees
        serializer = UserSerializer(attendees, many=True)
        return serializer.data

    class Meta:
        model = MyEvent
        fields = "__all__"
