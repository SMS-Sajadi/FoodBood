# Needed Imports for tokens handling
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib import messages
from .models import UserTable
from django.shortcuts import redirect


def activation_email(request, user, to_email):
    mail_subject = 'Activate your User account.'
    context = {
            'user': user.username,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            'protocol': 'https' if request.is_secure() else 'http'
    }
    message = render_to_string('template_activate_account.html', context=context)

    print(f"{context['protocol']}://{context['domain']}/accounts/activate/{context['uid']}/{context['token']}")
    # Comment these lines to prevent sending emails
    # email = EmailMessage(mail_subject, message, to=[to_email])
    # if email.send():
    #     messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
    #         received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    # else:
    #     messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserTable.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserTable.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('account_login_url')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect('home_page_url')
