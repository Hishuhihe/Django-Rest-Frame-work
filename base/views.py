from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# UserRegister
class UserRegisterAPIView(APIView):
    serializer_class = UserSerializer
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)


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


# Chưa hoàn thành 
# class LogoutAPIView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     @csrf_exempt
#     def post(self, request, *args, **kwargs):
#         # Remove Token from User
#         request.user.access_token.delete()
#         return JsonResponse({
#                 'message': 'logout successful!'
#             }, status=status.HTTP_201_CREATED)
        
    
   


        