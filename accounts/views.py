# Needed Imports for views
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import UserTable
from .forms import UserRegisterForm, UserLoginForm, UserPasswordRestEmailForm, UserInfoUpdateForm
from .email_verification import activation_email
from .forget_password import password_forget_email
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


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
            return render(request=request, template_name="register.html", context={"form": form}, status=400)

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
            elif UserTable.objects.filter(email=cleaned_data['email']).exists():
                check_user = UserTable.objects.get(email=cleaned_data['email'])
                password = cleaned_data['password']
                if check_user is not None and check_user.check_password(password):
                    messages.error(request, "You Should Verify Your Email First!", "danger")
                else:
                    messages.error(request, "Check your username and password!", "danger")
                return render(request=request, template_name="login.html", context={"form": form}, status=404)
            else:
                return HttpResponseForbidden()

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return render(request=request, template_name="login.html", context={"form": form}, status=404)

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


class UserInfoUpdate(LoginRequiredMixin, View):
    """
    This is the basic class for updating user information on setting page.
    """
    def post(self, request):
        form = UserInfoUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = request.user
            user.name = cleaned_data['name']
            user.phone_number = cleaned_data['phone_number']
            if cleaned_data['profile_pic'] == False:
                user.profile_pic = None
            elif len(form.files) != 0:
                user.profile_pic = cleaned_data['profile_pic']
            user.save()
            messages.success(request, "Your Info Updated")
            return redirect('setting_page_url')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('setting_page_url')

    # A Temp get for test purposes
    def get(self, request):
        form = UserInfoUpdateForm(instance=request.user)
        return render(request, template_name='Temp_User_info_udate.html', context={'form': form})
