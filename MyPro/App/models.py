from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.urls import reverse


# from django.contrib.auth.models import User


# Create your models here.
from App import forms


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    supplier_location = models.CharField(max_length=50)
    supplier_description = models.CharField(max_length=100)

    def __str__(self):
        return self.supplier_name


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_id = models.IntegerField()
    product_description = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


# class User(AbstractUser):
#     location = models.CharField(max_length=30, blank=True)
#     OrgName = models.CharField(max_length=50, blank=True)

# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete='CASCADE')
#
#     location = models.CharField(max_length=30, blank=True)
#     OrgName = models.CharField(max_length=50, blank=True)
#
#     # USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = ['firstname', 'lastname', 'password']
#
#
# def __str__(self):
#     return self.user.username


# class MyAccountManger(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have an email address")
#
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#
# class Account(AbstractBaseUser):
#     email = models.EmailField(verbose_name='email', max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', ]
#
#     objects = MyAccountManger()
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     def has_module_perms(self, app_label):
#         return True



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')
    location = models.CharField(max_length=100, default='')
    OrgName = models.CharField(max_length=100, default='')
    role = models.CharField(max_length=100,default='')
    failure_login_attempts = models.IntegerField('Failure Attempts', default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', ]

    def __str__(self):
        return self.user.username


class PasswordResetHistory(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')
    login_time = models.TimeField(auto_now=True)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username

