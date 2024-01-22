
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Order
from .forms import PromoCodeForm


class OrdersList(LoginRequiredMixin, View):
    """
    This is the basic class for showing all user orders
    """
    def get(self, request):
        user = request.user
        orders = user.orders.all()

        return render(request, template_name='Orders_list_template.html', context={'orders': orders})


class OrdersAddPromo(LoginRequiredMixin, View):
    """
    This is the basic class for showing all user orders
    """
    def post(self, request, order_id):
        user = request.user
        try:
            order = user.orders.get(id=order_id)
        except Order.DoesNotExist:
            messages.error(request, "Order Not Found!")
            return redirect('home_page_url')

        form = PromoCodeForm(request.POST)
        if form.is_valid():
            order.promo_code = form.cleaned_data['promo_code']
            order.save()
            messages.success(request, "Promo Code Added Successfully")
        else:
            messages.error(request, 'Promo Code is Invalid!')

        return redirect('orders_list_url')

    # A Temporary get function for testing
    def get(self, request, order_id):
        form = PromoCodeForm()
        return render(request, template_name='Temp_Promo_add.html', context={'form': form})
