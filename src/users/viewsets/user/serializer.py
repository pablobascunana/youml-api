from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'username', 'name', 'lastname', 'email')
        read_only_fields = ('username', 'name', 'lastname', 'uuid', 'verified', 'register_date')
        extra_kwargs = {
            'password': {'write_only': True}
        }
