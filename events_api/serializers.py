from rest_framework import serializers
from buildings.models import (
    MyEvent,
)


class MyEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyEvent
        fields = "__all__"
