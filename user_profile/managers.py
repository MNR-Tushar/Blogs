from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password, **extra_fields):
        if not username:
            raise ValueError("The user must be set")
        
        if not email:
            raise ValueError("The email must be set")
        
        if not password:
            raise ValueError("The password must be set")
        
        email=self.normalize_email(email)
        user=self.model(username,email,password,**extra_fields)
        user.set_password(password)
        user.save()

    def create_superuser(self,username,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("The superuser must have is_staff=True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("The superuser must have is_superuser=True")
        
        return self.create_user(username,email,password,**extra_fields)