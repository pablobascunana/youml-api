from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'username', 'name', 'lastname', 'email', 'password', 'role')
        extra_kwargs = {
            'password': {'write_only': True}
        }
