from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from foods.models import Cart, Food
from resturants.models import Restaurant


class UserTableManager(BaseUserManager):
    """
    This class is for removing the username form model.
    By this Manager there will be no need to enter the username filed for saving the model in DB.
    """
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email).lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UserTable(AbstractUser):
    """
    This is the Base User Model of the System
    """
    first_name = None
    last_name = None
    username = None
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True)

    # Setting the Email as the username field for login
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # cart = models.Model
    fav_food = models.ManyToManyField(Food)
    fav_rest = models.ManyToManyField(Restaurant)

    profile_pic = models.ImageField(null=True, blank=True, upload_to="accounts/static/profile_pictures/")

    objects = UserTableManager()

    def __str__(self):
        return self.name + " : " + self.email


