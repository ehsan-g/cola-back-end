from django.urls import path
from .views import BuildingList

app_name = "blog_api"

urlpatterns = [
    path("", BuildingList.as_view(), name="list-buildings"),
]
