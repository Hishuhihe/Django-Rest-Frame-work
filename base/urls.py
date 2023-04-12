
from django.urls import path
from .views import UserRegisterAPIView, LoginView, LogoutView, AllUserListView, UserDestroyAPIView, UserUpdateView

urlpatterns = [
    path('api/register', UserRegisterAPIView.as_view(), name='user-register'),
    path('api/login', LoginView.as_view(), name='login'),
    path('api/logout', LogoutView.as_view(), name='logout'),
    path('api/all/users/', AllUserListView.as_view(), name='user-list'),
    path('api/update/users/<int:id>', UserUpdateView.as_view(), name='update-user'),
    path('api/delete/users/<int:id>/', UserDestroyAPIView.as_view(), name='destroy-user'),
    
]
