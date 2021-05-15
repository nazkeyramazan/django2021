from rest_framework import serializers
from .models import MainUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validated_data):
        user = MainUser.objects.create_user(email=validated_data['email'],
                                            password=validated_data['password'],
                                            first_name=validated_data['first_name'],
                                            last_name=validated_data['last_name']
                                            )

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = '__all__'