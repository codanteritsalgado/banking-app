from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User, Transaction

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'address', 'phone_number', 'profile_picture', 'password']
        extra_kwargs = {
            'profile_picture': {'required': False}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'amount', 'date', 'transaction_type']
