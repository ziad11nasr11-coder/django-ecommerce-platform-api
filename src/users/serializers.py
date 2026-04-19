from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    user_type = serializers.ChoiceField(
        choices=[
            ('seller', 'Seller'),
            ('customer', 'Customer'),
        ]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password', 'user_type']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context['request'].user

        if not user.check_password(data['old_password']):
            raise serializers.ValidationError("Old password is incorrect")

        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = ['country', 'city', 'address', 'is_verified']

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['city', 'address']

class UserProfileSerializer(serializers.ModelSerializer):
    seller_profile = SellerProfileSerializer(required=False)
    customer_profile = CustomerProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'seller_profile', 'customer_profile']

