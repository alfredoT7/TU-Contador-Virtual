from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser
from django.utils import timezone

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Deberias meter un emal valido')
        
        email = email.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_short_name(self):
        return self.first_name
    

class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transactions')
    amount = models.FloatField()
    date = models.models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

class Account(models.Model):
    user = models.ManyToManyField(User, on_delete=models.CASCADE, related_name='user_account')
    balance = models.FloatField()
    date = models.models.DateTimeField(default=timezone.now)
