
from django.urls import path
from .views import UserRegisterAPIView, LoginView, LogoutView, AllUserListView, UserDestroyAPIView, UserUpdateView

urlpatterns = [
    path('register', UserRegisterAPIView.as_view(), name='user-register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('all/users/', AllUserListView.as_view(), name='user-list'),
    path('update/users/<int:id>', UserUpdateView.as_view(), name='update-user'),
    path('delete/users/<int:id>/', UserDestroyAPIView.as_view(), name='destroy-user'),
    
]
