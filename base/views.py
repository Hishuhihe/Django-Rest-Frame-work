from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers

# UserRegister
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
    @csrf_exempt
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return JsonResponse({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
   


        