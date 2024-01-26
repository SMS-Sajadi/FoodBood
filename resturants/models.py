from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Restaurant(models.Model):
    name = models.CharField(max_length=256, unique=True)
    restaurant_icon = models.ImageField(null=True, blank=True, upload_to="resturants/static/resturant_icons/")
    restaurant_header_pic = models.ImageField(null=True, blank=True, upload_to="resturants/static/resturant_header_pics/")

    description = models.TextField(null=True, blank=True)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    num_rating = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    res_class_chioces = (
        ('1', '$'),
        ('2', '$$'),
        ('3', '$$$')
    )
    restaurant_class = models.CharField(max_length=1, choices=res_class_chioces)
    address = models.CharField(max_length=500, null=False, default="Isfahan")

    free_delivery = models.BooleanField(default=True)

    categ = models.CharField(max_length=32, default="Burger", null=False, blank=False)

    def __str__(self):
        return self.name
