from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, phone number, username and password.
        """
        if not email and not phone_number:
            raise ValueError('The Email or Phone Number field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        
        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, username, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, phone number, username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, phone_number, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    objects = UserManager()

    def __str__(self):
        return self.username
