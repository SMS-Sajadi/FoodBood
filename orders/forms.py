from django import forms
from .models import Order, OrderItem


class PromoCodeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['promo_code']


class OrderItemAddForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['num']
