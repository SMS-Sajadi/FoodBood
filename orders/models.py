from django.db import models
from accounts.models import UserTable
from resturants.models import Restaurant
from foods.models import Food
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver


class Order(models.Model):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')

    price = models.DecimalField(default=0, decimal_places=2, max_digits=10, null=False, blank=True,
                                validators=[MinValueValidator(0)])

    final_price = models.DecimalField(default=0, decimal_places=2, max_digits=10, validators=[MinValueValidator(0)],
                                      null=False, blank=True)

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
        return (str(self.id) + ":" + self.user.name + ":" + self.restaurant.name + ":"
                + str(self.time.month) + "-" + str(self.time.day))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='order_items')
    num = models.IntegerField(default=1, null=False, blank=False, validators=[MinValueValidator(1)])
    price = models.FloatField(default=0, null=False, blank=True, validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.order.id) + ":" + self.food.name


@receiver([pre_save], sender=OrderItem)
def update_orderitem_price(sender, instance, **kwargs):
    food = instance.food
    instance.price = food.price * instance.num


@receiver([post_save, post_delete], sender=OrderItem)
def update_order_price_caller(sender, instance, **kwargs):
    instance.order.save()


@receiver([pre_save], sender=Order)
def update_order_price(sender, instance, **kwargs):
    try:
        order_items = instance.items.all()
    except Exception:
        instance.price = 0
        instance.final_price = 0
        return

    price = 0
    for item in order_items:
        price += item.price

    instance.price = price
    instance.final_price = price if not instance.promo_code else price - 0.1 * price
