from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import (
    MyUser,
)


from rest_framework import serializers
from users.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    permission_level = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = MyUser
        fields = ("email", "user_name", "password", "permission_level")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        #  Both get() and pop() return items, but pop() removes them from the source dict, while get() leaves them there.
        password = validated_data.pop("password")
        # as long as the fields are the same, we can just use this
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return


class UserSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField(read_only=True)
    first_name = serializers.SerializerMethodField(read_only=True)
    last_name = serializers.SerializerMethodField(read_only=True)
    employee_number = serializers.SerializerMethodField(read_only=True)
    profile_picture = serializers.SerializerMethodField(read_only=True)
    wallet_address = serializers.SerializerMethodField(read_only=True)
    nft_address = serializers.SerializerMethodField(read_only=True)
    permission_level = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)
    is_superuser = serializers.SerializerMethodField(read_only=True)
    is_staff = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MyUser
        fields = [
            "id",
            "user_name",
            "first_name",
            "last_name",
            "employee_number",
            "profile_picture",
            "wallet_address",
            "nft_address",
            "permission_level",
            "is_admin",
            "is_superuser",
            "is_staff",
            "company",
            "my_event_attendees",
        ]

    def get_user_name(self, obj):
        return obj.user_name  # email

    def get_first_name(self, obj):
        return obj.first_name

    def get_last_name(self, obj):
        return obj.last_name

    def get_employee_number(self, obj):
        return obj.employee_number

    def get_profile_picture(self, obj):
        if obj.profile_picture:
            return obj.profile_picture.url

    def get_wallet_address(self, obj):
        return obj.wallet_address

    def get_nft_address(self, obj):
        return obj.nft_address

    def get_permission_level(self, obj):
        return obj.permission_level

    def get_is_admin(self, obj):
        return obj.is_admin

    def get_is_superuser(self, obj):
        return obj.is_superuser

    def get_is_staff(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MyUser
        fields = [
            "id",
            "user_name",
            "first_name",
            "last_name",
            "employee_number",
            "profile_picture",
            "wallet_address",
            "nft_address",
            "permission_level",
            "is_admin",
            "is_superuser",
            "is_staff",
            "token",
        ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        # our token is going to be an access token not refresh one
        return str(token.access_token)
