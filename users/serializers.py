from rest_framework import serializers
from users.models import NewUser


class MyUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ("email", "user_name", "password")
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
