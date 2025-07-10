from django.contrib.auth.models import BaseUserManager

class CustomUserMnager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required!")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)         
        user.save()
        return user
    
    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("SuperUser must be is_staff")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("SuperUser must be is_superuser")
        if extra_fields.get("is_active") is not True:
            raise ValueError("SuperUser must be is_active")
        return self.create_user(email, username, password, **extra_fields)