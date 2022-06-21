from django.urls import path
from django.urls import include, re_path
from .views import BuildingList
from buildings_api.views import get_building_floor

app_name = "buildings_api"

urlpatterns = [
    re_path(r"^getBuildings/$", get_building_floor),
    path("", BuildingList.as_view(), name="list-buildings"),
]
