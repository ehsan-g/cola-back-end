from django.urls import path
from .views import MyTokenObtainPairView, ProfileView

app_name = "users_api"

urlpatterns = [
    path("login", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("profile-view", ProfileView.as_view(), name="user_profile-view"),
]
