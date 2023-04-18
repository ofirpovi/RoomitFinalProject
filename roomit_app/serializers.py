from datetime import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Info


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
        #print("create: {}".format(validated_data))
        #print(validated_data)
        email = validated_data['email']
        password = make_password(validated_data['password'])
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        print("create user: {}".format(user))
        return user


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
        

    def validate(self,data):
        print('validate')
        if self.instance is None:
            # if this is a new instance, we need to validate the user_id field
            if Info.objects.filter(User_ID=data['User_ID']).exists():
                raise serializers.ValidationError('Profile for this user already exists.')
        else:
            # if this is an existing instance, we need to make sure the user_id hasn't changed
            if 'User_ID' in data and data['User_ID'] != self.instance.User_ID:
                raise serializers.ValidationError('User ID cannot be changed.')

        # validate the First_Name field
        if not data.get('First_Name'):
            raise serializers.ValidationError('First name is required.')

        # validate the Last_Name field
        if not data.get('Last_Name'):
            raise serializers.ValidationError('Last name is required.')

        # validate the Birthdate field
        if not data.get('Birthdate'):
            raise serializers.ValidationError('Birthdate is required.')
        elif data['Birthdate'] > timezone.now().date():
            raise serializers.ValidationError('Birthdate cannot be in the future.')

        # validate the Phone_Number field
        if not data.get('Phone_Number'):
            raise serializers.ValidationError('Phone number is required.')

        # validate the Gender field
        gender_choices = dict(Info.GENDER_CHOICES)
        if 'Gender' in data and data['Gender'] not in gender_choices:
            raise serializers.ValidationError(f'Invalid gender choice. Must be one of {", ".join(gender_choices.values())}.')

        # validate the Occupation field
        occupation_choices = dict(Info.OCCUPATION_CHOICES)
        if 'Occupation' in data and data['Occupation'] not in occupation_choices:
            raise serializers.ValidationError(f'Invalid occupation choice. Must be one of {", ".join(occupation_choices.values())}.')

        # validate the Smoker field
        smoker_choices = dict(Info.SMOKER_CHOICES)
        if 'Smoker' in data and data['Smoker'] not in smoker_choices:
            raise serializers.ValidationError(f'Invalid smoker choice. Must be one of {", ".join(smoker_choices.values())}.')

        # validate the Diet field
        diet_choices = dict(Info.DIET_CHOICES)
        if 'Diet' in data and data['Diet'] not in diet_choices:
            raise serializers.ValidationError(f'Invalid diet choice. Must be one of {", ".join(diet_choices.values())}.')

        # validate the Status field
        status_choices = dict(Info.STATUS_CHOICES)
        if 'Status' in data and data['Status'] not in status_choices:
            raise serializers.ValidationError(f'Invalid status choice. Must be one of {", ".join(status_choices.values())}.')

        # validate the Hospitality field
        if 'Hospitality' in data and not isinstance(data['Hospitality'], bool):
            raise serializers.ValidationError('Invalid hospitality choice. Must be a boolean.')

        # validate the Kosher field
        if 'Kosher' in data and not isinstance(data['Kosher'], bool):
            raise serializers.ValidationError('Invalid kosher choice. Must be a boolean.')

        return data
