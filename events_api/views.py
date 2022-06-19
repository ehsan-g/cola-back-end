from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import MyEventSerializer
from django.db.models import Q
from buildings.models import Room, MyEvent
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import (
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class EventList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MyEventSerializer
    queryset = MyEvent.objects.all()


# class EventList(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]

#     def get(self, request, *args, **kwargs):
#         room = Room.objects.get(id=kwargs["roomId"])
#         events = room.my_events_room.all()
#         serializer = MyEventSerializer(events, many=True)
#         return Response({"events": serializer.data})

#     def post(self, request, *args, **kwargs):
#         event = MyEvent.objects.get(pk=kwargs["eventId"])
#         user = request.user
#         id = request.user.id

#         attendees = event.attendees.all()
#         if user not in attendees:
#             event.attendees.add(user.id)
#             event.save()
#             serializer = MyEventSerializer(event, many=False)
#             return Response({"event": serializer.data})

#         try:
#             attendees = event.attendees.all()
#             if user not in attendees:
#                 event.attendees.add(user)
#                 event.save()
#                 serializer = MyEventSerializer(event, many=False)
#                 return Response({"event": serializer.data})

#         except:
#             data = {"detail": "Attendee could not join"}
#             return Response(data, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         event = MyEvent.objects.get(pk=kwargs["eventId"])
#         user = request.user
#         try:
#             event.attendee = user
#             event.delete()
#         except:
#             data = {"detail": "Attendee could not join"}
#             return Response(data, status=status.HTTP_204_NO_CONTENT)
