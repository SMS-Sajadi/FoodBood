from django import forms
from .models import Address


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address']


class AddressForm(forms.Form):
    address = forms.CharField(max_length=256)
