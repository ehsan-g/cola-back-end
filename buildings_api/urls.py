from django.urls import path
from .views import BuildingList

app_name = "building_api"

urlpatterns = [
    path("", BuildingList.as_view(), name="list-buildings"),
]
