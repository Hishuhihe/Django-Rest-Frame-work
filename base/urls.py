from django.urls import path
from .views import UserRegisterAPIView, LoginView, LogoutAPIView

urlpatterns = [
    path('api/register', UserRegisterAPIView.as_view(), name='user-register'),
    path('api/login', LoginView.as_view(), name='login'),
    path('api/logout', LogoutAPIView.as_view(), name='logout')
]
