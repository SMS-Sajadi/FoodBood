from django.db import models
from accounts.models import UserTable
from resturants.models import Restaurant
from foods.models import Food
from django.core.validators import MinValueValidator


class Order(models.Model):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    price = models.FloatField(default=0, null=False, blank=True, validators=[MinValueValidator(0)])
    promo_code = models.CharField(max_length=8, null=True, blank=True)

    status_choices = (
        ('1', 'Cart'),
        ('2', 'Up Coming'),
        ('3', 'Completed'),
        ('4', 'Canceled')
    )

    status = models.CharField(max_length=1, default='1', choices=status_choices, null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":" + self.restaurant.name + ":" + str(self.time.month) + "-" + str(self.time.day)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='order_items')
    num = models.IntegerField(default=1, null=False, blank=False, validators=[MinValueValidator(1)])
    price = models.FloatField(default=0, null=False, blank=True, validators=[MinValueValidator(0)])
