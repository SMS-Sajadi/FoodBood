# Needed Imports for tokens handling
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import password_reset_token
from django.contrib import messages
from .models import UserTable
from django.shortcuts import redirect, render
from .forms import UserPasswordResetPassForm


def password_forget_email(request, user, to_email):
    mail_subject = 'Password Forgotten?'
    context = {
            'user': user.username,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': password_reset_token.make_token(user),
            'protocol': 'https' if request.is_secure() else 'http'
    }
    message = render_to_string('template_reset_password.html', context=context)

    print(f"{context['protocol']}://{context['domain']}/accounts/passreset/{context['uid']}/{context['token']}")
    # Comment these lines to prevent sending emails
    # email = EmailMessage(mail_subject, message, to=[to_email])
    # if email.send():
    #     messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
    #         received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    # else:
    #     messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def reset(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserTable.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserTable.DoesNotExist):
        user = None

    if user is not None and password_reset_token.check_token(user, token):
        if request.method == "GET":
            context = {
                'form': UserPasswordResetPassForm()
            }
            return render(request, template_name='password_reset.html', context=context)
        else:
            form = UserPasswordResetPassForm(request.POST)
            if form.is_valid():
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, 'Your Password was reset.')
            else:
                messages.error(request, 'Password is not acceptable!')

            return redirect('account_login_url')
    else:
        messages.error(request, 'Password Reset link is invalid!')

    return redirect('account_login_url')
