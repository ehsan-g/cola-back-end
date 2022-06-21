from django.urls import path
from .views import MyUserCreate

app_name = "users"

urlpatterns = [
    path("create/", MyUserCreate.as_view(), name="create_user"),
]
