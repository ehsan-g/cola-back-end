from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users_api.serializers import (
    UserSerializerWithToken,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MyUserSerializer

#  Customizing token claims with JWT / overriding
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims, meaning when token decrypted more data is available check jwt.io
        token["username"] = user.user_name
        token["message"] = "hello world"
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # data['username'] = self.user.username
        # data['email'] = self.user.email
        #  ...
        # refactored to the following:
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = MyUserSerializer(user, many=False)
        return Response(serializer.data)
