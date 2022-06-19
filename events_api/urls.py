from .views import EventList
from rest_framework.routers import DefaultRouter

app_name = "event_api"
router = DefaultRouter()
router.register("", EventList, basename="list-events")
# router.register("rooms/<int:roomId>", EventList, basename="room-events")
urlpatterns = router.urls


# urlpatterns = [
#     # path("register/<int:eventId>", EventList.as_view(), name="register-events"),
#     # path("unregister/int:eventId>", EventList.as_view(), name="unregister-events"),
#     path("rooms/<int:roomId>", EventList.as_view(), name="list-events"),
# ]
