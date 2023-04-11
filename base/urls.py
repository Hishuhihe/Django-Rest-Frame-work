from django.urls import path
from .views import UserRegisterAPIView, LoginView, LogoutView

urlpatterns = [
    path('api/register', UserRegisterAPIView.as_view(), name='user-register'),
    path('api/login', LoginView.as_view(), name='login'),
    path('api/logout', LogoutView.as_view(), name='logout') 
]
