from django.urls import path
from .views import EventList

app_name = "event_api"

urlpatterns = [
    # path("register/<int:eventId>", EventList.as_view(), name="register-events"),
    # path("unregister/int:eventId>", EventList.as_view(), name="unregister-events"),
    path("rooms/<int:roomId>", EventList.as_view(), name="list-events"),
]
