from django import forms
from .models import UserTable


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserTable
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Mark'}),
            'email': forms.EmailInput(attrs={'placeholder': 'mark@gmail.com'}),
            'password': forms.PasswordInput(attrs={'placeholder': '*****'})
        }
        labels = {
            'name': 'FULL NAME',
            'email': 'EMAIL ADDRESS',
            'password': 'PASSWORD'
        }


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=256, label='EMAIL ADDRESS', widget=forms.EmailInput(attrs={'placeholder': 'mark@gmail.com'}))
    password = forms.CharField(max_length=256, label='PASSWORD', widget=forms.PasswordInput(attrs={'placeholder': '*****'}))


class UserPasswordRestEmailForm(forms.Form):
    email = forms.EmailField(max_length=256, label='EMAIL ADDRESS', widget=forms.EmailInput(attrs={'placeholder': 'mark@gmail.com'}))


class UserPasswordResetPassForm(forms.Form):
    password = forms.CharField(max_length=256, label='PASSWORD', widget=forms.PasswordInput(attrs={'placeholder': '*****'}))


class UserInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = UserTable
        fields = ['name', 'phone_number', 'profile_pic']
