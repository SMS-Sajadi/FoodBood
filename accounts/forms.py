from django import forms
from .models import UserTable


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserTable
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=256)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput)


class UserPasswordRestEmailForm(forms.Form):
    email = forms.EmailField(max_length=256)


class UserPasswordResetPassForm(forms.Form):
    password = forms.CharField(max_length=256, widget=forms.PasswordInput)


class UserInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = UserTable
        fields = ['name', 'phone_number', 'profile_pic']
