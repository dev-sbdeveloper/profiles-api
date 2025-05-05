from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for UserProfile model."""

    def create_user(self, email, name, password=None):
        """Create a new user profile."""
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        """Create a new superuser profile."""
        user = self.create_user(email, name, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Custom user profile model that uses email as the unique identifier."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Retrieve full name of the user."""
        return self.name

    def get_short_name(self):
        """Retrieve short name of the user."""
        return self.name

    def __str__(self):
        return self.email
