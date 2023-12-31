import uuid

from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(default=uuid.uuid4)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'full_name', 'status', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instace, validated_data):
        user = super().update(instace, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user
    
