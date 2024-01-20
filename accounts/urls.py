from django.urls import path
from . import views, email_verification, forget_password


urlpatterns = [
    path('activate/<uidb64>/<token>', email_verification.activate, name='account_activation_url'),
    path('register/', views.UserRegister.as_view(), name='account_register_url'),
    path('login/', views.UserLogin.as_view(), name='account_login_url'),
    path('logout/', views.UserLogout.as_view(), name='account_logout_url'),
    path('password_forget/', views.UserPasswordReset.as_view(), name='account_password_forget_url'),
    path('passreset/<uidb64>/<token>', forget_password.reset, name='account_password_reset_url'),
]
