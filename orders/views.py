
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseForbidden
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Order, OrderItem
from .forms import PromoCodeForm, OrderItemAddForm
from foods.models import Food


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
    This is the basic class for handling the user adding promo codes
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


class OrderItemAdd(LoginRequiredMixin, View):
    """
    In this class we handle the item adding for the carts
    """
    def post(self, request, food_id):
        user = request.user
        try:
            food = Food.objects.get(id=food_id)
        except Exception:
            messages.error(request, "The Food Was not Found!")
            raise Http404(request)

        rest = food.restaurant

        order, created = rest.orders.get_or_create(user=user, status='1')

        form = OrderItemAddForm(request.POST)

        if not form.is_valid():
            messages.error(request, "The number entered is not correct!")
            return redirect('home_page_url')

        num = form.cleaned_data['num']

        if created:
            order_item = OrderItem(order=order, food=food, num=num)
        else:
            order_item, order_item_created = order.items.get_or_create(food=food)
            if not order_item_created:
                order_item.num += num
            else:
                order_item.num = num

        order_item.save()
        messages.success(request, "Item Added Successfully!")
        return redirect('home_page_url')

    # A Temporary Function for adding foods to cart
    def get(self, request, food_id):
        form = OrderItemAddForm()
        return render(request, 'Temp_Promo_add.html', {'form': form})


class OrderItemDelete(LoginRequiredMixin, View):
    """
    In this class we handle the item deleting the items from carts
    """
    def get(self, request, orderitem_id):
        user = request.user
        try:
            order_item = OrderItem.objects.get(id=orderitem_id)
        except Exception:
            messages.error(request, "The OrderItem Was not Found!")
            raise Http404(request)

        order = order_item.order

        if order.user != user or order.status != '1':
            return HttpResponseForbidden(request)

        order_item.delete()

        if not order.items.exists():
            order.delete()

        messages.success(request, "Item Deleted Successfully")
        return redirect('home_page_url')


class OrderCheckout(LoginRequiredMixin, View):
    """
    In this class we handle the order checkout option
    """
    def get(self, request, order_id):
        user = request.user
        try:
            order = Order.objects.get(id=order_id, status='1')
        except Exception:
            messages.error(request, "The Order Was not Found!")
            raise Http404(request)

        if order.user != user:
            return HttpResponseForbidden(request)

        order.status = '2'
        order.save()

        messages.success(request, "The Order Checked Out!")
        return redirect('orders_list_url')


class OrderCancel(LoginRequiredMixin, View):
    """
    In this class we handle the order cancel option
    """
    def get(self, request, order_id):
        user = request.user
        try:
            order = Order.objects.get(id=order_id, status='2')
        except Exception:
            messages.error(request, "The Order Was not Found!")
            raise Http404(request)

        if order.user != user:
            return HttpResponseForbidden(request)

        order.status = '4'
        order.save()

        messages.success(request, "The Order Canceled")
        return redirect('orders_list_url')
