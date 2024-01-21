from django import forms
from .models import Address


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address']
