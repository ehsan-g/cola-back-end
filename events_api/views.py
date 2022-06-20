from rest_framework.response import Response
from .serializers import MyEventSerializer
from buildings.models import Room, MyEvent
from users.models import MyUser
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework import status


class EventList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MyEventSerializer

    def get_queryset(self):
        return MyEvent.objects.all()


class UserEventList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MyEventSerializer

    def get_queryset(self):
        user = self.request.user
        return user.my_event_attendees.all()


class EventDetail(generics.RetrieveAPIView):
    serializer_class = MyEventSerializer

    def get_object(self, queryset=None, **kwargs):
        id = self.kwargs.get("pk")
        return get_object_or_404(MyEvent, id=id)


class RoomEvents(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MyEventSerializer

    def get_queryset(self, *args, **kwargs):
        roomId = self.kwargs.get("roomId", None)
        return MyEvent.objects.filter(room_id=roomId)


# no use case for this app
class EventListFilter(generics.ListAPIView):

    queryset = MyEvent.objects.all()
    serializer_class = MyEventSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ["=id"]


class EventRegister(generics.UpdateAPIView):
    serializer_class = MyEventSerializer

    def update(self, request, *args, **kwargs):
        event = MyEvent.objects.get(pk=kwargs["eventId"])
        user = MyUser.objects.get(pk=kwargs["userId"])
        event.attendees.add(user)
        event.save()
        user.save()
        return Response({"message": f"{user.first_name} registered successfully"})

    def delete(self, request, *args, **kwargs):
        event = MyEvent.objects.get(pk=kwargs["eventId"])
        user = MyUser.objects.get(pk=kwargs["userId"])
        event.attendees.remove(user)
        event.save()
        return Response({"message": f"{user.first_name} un-registered successfully"})

    # def post(self, request, *args, **kwargs):
    #     serializer = MyEventSerializer(data=request.data)
    #     event = MyEvent.objects.get(pk=kwargs["eventId"])
    #     user = request.user
    #     id = request.user.id
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     attendees = event.attendees.all()
    #     if user not in attendees:
    #         event.attendees.add(user.id)
    #         event.save()
    #         serializer = MyEventSerializer(event, many=False)
    #         return Response({"event": serializer.data})

    #     try:
    #         attendees = event.attendees.all()
    #         if user not in attendees:
    #             event.attendees.add(user)
    #             event.save()
    #             serializer = MyEventSerializer(event, many=False)
    #             return Response({"event": serializer.data})

    #     except:
    #         data = {"detail": "Attendee could not join"}
    #         return Response(data, status=status.HTTP_400_BAD_REQUEST)


# class CreatePost(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
#         print(request.data)
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EventList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = MyEventSerializer
#     events = MyEvent.objects.all()

#     def list(self, request):
#         serializer = MyEventSerializer(self.events, many=True)
#         return Response({"events": serializer.data})

#     def retrieve(self, request, pk=None, **kwargs):
#         room = get_object_or_404(Room, id=pk)
#         serializer = MyEventSerializer(self.events, many=True)
#         return Response({"events": serializer.data})


# class EventList(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]

#     def get(self, request, *args, **kwargs):
#         room = Room.objects.get(id=kwargs["roomId"])
#         events = room.my_events_room.all()
#         serializer = MyEventSerializer(events, many=True)
#         return Response({"events": serializer.data})

#     def post(self, request, *args, **kwargs):
# event = MyEvent.objects.get(pk=kwargs["eventId"])
# user = request.user
# id = request.user.id

# attendees = event.attendees.all()
# if user not in attendees:
#     event.attendees.add(user.id)
#     event.save()
#     serializer = MyEventSerializer(event, many=False)
#     return Response({"event": serializer.data})

# try:
#     attendees = event.attendees.all()
#     if user not in attendees:
#         event.attendees.add(user)
#         event.save()
#         serializer = MyEventSerializer(event, many=False)
#         return Response({"event": serializer.data})

# except:
#     data = {"detail": "Attendee could not join"}
#     return Response(data, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         event = MyEvent.objects.get(pk=kwargs["eventId"])
#         user = request.user
#         try:
#             event.attendee = user
#             event.delete()
#         except:
#             data = {"detail": "Attendee could not join"}
#             return Response(data, status=status.HTTP_204_NO_CONTENT)
