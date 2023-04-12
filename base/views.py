from rest_framework import status, generics
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.generics import DestroyAPIView, UpdateAPIView,  RetrieveAPIView


User = get_user_model()
# UserRegisterandcreat
class UserRegisterAPIView(APIView):
    serializer_class = UserSerializer

    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return JsonResponse({
                'error_message': str(e),
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return JsonResponse({
            'message': 'Register successful!'
        }, status=status.HTTP_201_CREATED)


# UserLogin               
class LoginView(APIView):
    """
    API view for user login
    """
    serializer_class = LoginSerializer
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return JsonResponse(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'error_message': 'Try again',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)

#Userlogout
class LogoutView(APIView):
    """
    API view to handle user logout
    """
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return JsonResponse({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class AllUserListView(generics.ListAPIView):
    """
    API view to list all users or create a new user
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Get queryset for all active users
        """
        return User.objects.filter(is_active=True)
    
class UserUpdateView(RetrieveAPIView, UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        # Get the current instance
        instance = self.get_object()
        # Save the old values of email and phone_number
        old_email = instance.email
        old_phone_number = instance.phone_number
        # Update the instance with the new values
        serializer.save()
        # Check if email and phone_number havegs)


class UserDestroyAPIView(DestroyAPIView):
    """
    API view to delete a user
    
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

        