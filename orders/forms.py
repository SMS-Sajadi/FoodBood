from django import forms
from .models import Order


class PromoCodeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['promo_code']
