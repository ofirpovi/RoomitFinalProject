from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from . import models


class UserSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def validate(self, data):
        print("validate: {}".format(data))
        confirm_password = self.initial_data.get('confirm_password')
        if data['password'] != confirm_password:
            raise serializers.ValidationError(
                "Both passwords are not matching")
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email is already taken")
        return data

    def create(self, validated_data):
        print("create: {}".format(validated_data))
        print(validated_data)
        email = validated_data['email']
        password = make_password(validated_data['password'])
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        print("create user: {}".format(user))
        return user


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Info
        fields = ('User_ID', 'First_Name', 'Last_Name', 'Phone_Number', 'Birthdate', 'Gender',
                  'Occupation', 'Smoker', 'Diet', 'Kosher', 'Status', 'Hospitality', 'Shopping')

    def create(self, validated_data):
        print("create: {}".format(validated_data))
        print(validated_data)
        info = models.Info.objects.create_Info(**validated_data)
        return info
