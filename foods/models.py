from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from resturants.models import Restaurant


class Food(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    food_pic = models.ImageField(null=True, blank=True, upload_to='foods/static/foods_pictures/')

    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    num_rating = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    category = models.CharField(max_length=64)

    price = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0)])

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return self.name


class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=32)
    foods = models.ManyToManyField(Food, related_name='rest_category', blank=True)

    def __str__(self):
        return self.name
