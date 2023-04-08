from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
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
