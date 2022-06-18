from django.urls import path
from .views import BuildingList, EventList

app_name = "blog_api"

urlpatterns = [
    path("", BuildingList.as_view(), name="list-buildings"),
    path("rooms/<int:roomId>/events", EventList.as_view(), name="list-events"),
]
