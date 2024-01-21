
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class OrdersList(LoginRequiredMixin, View):
    """
    This is the basic class for showing all user orders
    """
    def get(self, request):
        user = request.user
        orders = user.orders.all()

        return render(request, template_name='Orders_list_template.html', context={'orders': orders})
