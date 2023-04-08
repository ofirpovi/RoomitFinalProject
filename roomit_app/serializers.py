from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.Users
        fields = ('Email', 'Password')
        extra_kwargs = {
            'Password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def validate(self, data):
        print("validate: {}".format(data))
        confirm_password = self.initial_data.get('confirm_password')
        if data['Password'] != confirm_password:
            raise serializers.ValidationError(
                "Both passwords are not matching")
        if models.Users.objects.filter(Email=data['Email']).exists():
            raise serializers.ValidationError("Email is already taken")
        return data

    def create(self, validated_data):
        print("create: {}".format(validated_data))
        print(validated_data)
        user = models.Users.objects.create_user(**validated_data)
        return user
