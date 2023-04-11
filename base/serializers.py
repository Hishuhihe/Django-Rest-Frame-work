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
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'confirm_password', 'email', 'phone_number']
        extra_kwargs = {'id': {'required': False}}

    def validate_username(self, value):
        email = self.initial_data.get('email')
        phone_number = self.initial_data.get('phone_number')
        if not value and not email and not phone_number:
            raise serializers.ValidationError("At least one of the fields (Username, Email, Phone Number) must be set")
        return value

    def validate_email(self, value):
        if value and User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return value

    def validate_phone_number(self, value):
        if value and User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("This phone number is already in use.")
        return value

    def validate(self, attrs):
        """
        Validate the fields
        """
        password = attrs['password']
        confirm_password = attrs.pop('confirm_password', None)
        if password != confirm_password:
            raise serializers.ValidationError("The passwords do not match")
        if len(password) < 6 or len(password) > 8:
            raise serializers.ValidationError("Password must be between 6 and 8 characters long")
        attrs['password'] = make_password(password)
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


