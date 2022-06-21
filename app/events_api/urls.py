from .views import (
    EventList,
    RoomEvents,
    EventDetail,
    EventListFilter,
    EventRegister,
    UserEventList,
)
from rest_framework.routers import DefaultRouter
from django.urls import include, path

app_name = "event_api"
# router = DefaultRouter()
# router.register("", EventList, basename="list-events")
# router.register(r"rooms", EventList, basename="room-events")
# urlpatterns = router.urls


urlpatterns = [
    path("", EventList.as_view(), name="list-events"),
    path("event/<str:pk>", EventDetail.as_view(), name="event_detail"),
    path("mine", UserEventList.as_view(), name="user_eventsl"),
    path("search/", EventListFilter.as_view(), name="search-event"),
    path("rooms/<int:roomId>/", RoomEvents.as_view(), name="room-list-events"),
    path(
        "register/<int:eventId>/<int:userId>",
        EventRegister.as_view(),
        name="register-events",
    ),
]
