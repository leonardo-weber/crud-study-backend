from django.db import models
import uuid
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework.generics import CreateAPIView

class ProfileManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, uid, **extra_fields):
        user = self.model(id=uid, **extra_fields)
        user.save()
        return user

    def create_user(self, uid, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(uid, **extra_fields)

    def create_superuser(self, uid, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(uid, **extra_fields)

class Profile(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, max_length=48, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)

    objects = ProfileManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []

