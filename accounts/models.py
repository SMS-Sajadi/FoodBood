from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from foods.models import Food
from resturants.models import Restaurant


def phone_validate(value: str):
    if not value.isnumeric():
        raise ValidationError(f"{value} is not a correct phone number.")


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
    phone_number = models.CharField(max_length=11, null=True, blank=True, validators=[MinLengthValidator(11),
                                                                                      phone_validate])

    # Setting the Email as the username field for login
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    fav_food = models.ManyToManyField(Food, blank=True)
    fav_rest = models.ManyToManyField(Restaurant, blank=True)

    profile_pic = models.ImageField(default='accounts/static/profile_pictures/default_user.png', null=True, blank=True, upload_to="accounts/static/profile_pictures/")

    objects = UserTableManager()

    def __str__(self):
        return self.name + " : " + self.email

    def reset_pic(self):
        self.profile_pic = 'accounts/static/profile_pictures/default_user.png'
        self.save()
