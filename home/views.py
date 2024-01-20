from django.shortcuts import render, redirect
from django.views.generic import View


class HomePage(View):
    """
    This is the Basic Class for Handling User MainPage
    """
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, template_name="home_page.html")
        else:
            return redirect('account_login_url')
