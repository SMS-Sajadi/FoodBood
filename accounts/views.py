# Needed Imports for views
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserTable
from .forms import UserRegisterForm, UserLoginForm, UserPasswordRestEmailForm
from .email_verification import activation_email
from .forget_password import password_forget_email
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


class UserRegister(View):
    """
    This is the Basic Class for Handling User Registration
    """
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = UserTable.objects.create_user(
                email=cleaned_data['email'],
                password=cleaned_data['password'],
                name=cleaned_data['name']
            )
            user.save()
            activation_email(request, user, cleaned_data['email'])
            return redirect('account_login_url')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return render(request=request, template_name="register.html", context={"form": form})

    def get(self, request):
        form = UserRegisterForm()
        return render(request=request, template_name="register.html", context={"form": form})


class UserLogin(View):
    """
    This is the Basic Class for Handling User Login
    """
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['email'] = cleaned_data['email'].lower()
            user = authenticate(request, email=cleaned_data['email'], password=cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "User logged in successfully!", "success")
                return redirect('home_page_url')
            else:
                check_user = UserTable.objects.get(email=cleaned_data['email'])
                password = cleaned_data['password']
                if check_user is not None and check_user.check_password(password):
                    messages.error(request, "You Should Verify Your Email First!", "danger")
                else:
                    messages.error(request, "Check your username and password!", "danger")
                return render(request=request, template_name="login.html", context={"form": form})

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return render(request=request, template_name="login.html", context={"form": form})

    def get(self, request):
        form = UserLoginForm()
        return render(request=request, template_name="login.html", context={"form": form})


class UserLogout(View):
    """
    This is the Logout Class that will handle user loging out
    """
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully!", "success")
        return redirect('home_page_url')


class UserPasswordReset(View):
    """
    This is the Basic Class for Handling User Forgot Password
    """
    def post(self, request):
        form = UserPasswordRestEmailForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['email'] = cleaned_data['email'].lower()
            user = UserTable.objects.get(email=cleaned_data['email'])

            if user is not None:
                password_forget_email(request, user, cleaned_data['email'])
            else:
                messages.error(request, 'Email is incorrect!')

            return redirect('account_login_url')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return render(request=request, template_name="Forget_password.html", context={"form": form})

    def get(self, request):
        form = UserPasswordRestEmailForm()
        return render(request=request, template_name="Forget_password.html", context={"form": form})
