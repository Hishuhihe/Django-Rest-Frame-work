from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone_number']

    def validate(self, attrs):
        """
        Validate the fields
        """
        email = attrs.get('email')
        phone_number = attrs.get('phone_number')
        username = attrs.get('username')

        if not email and not phone_number:
            raise serializers.ValidationError("The Email or Phone Number field must be set")
        if not username:
            raise serializers.ValidationError("The Username field must be set")

        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email address is already in use.")
        if phone_number and User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("This phone number is already in use.")
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("This username is already in use.")

        attrs['password'] = make_password(attrs['password'])
        return attrs
    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        phone = attrs.get('phone')
        email = attrs.get('email')
        password = attrs.get('password')

        user = None
        if username:
            user = authenticate(username=username, password=password)
        elif phone:
            user = authenticate(phone=phone, password=password)
        elif email:
            user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials')

        if not user.is_active:
            raise serializers.ValidationError('User account is disabled')

        refresh = RefreshToken.for_user(user)
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)

        return attrs

