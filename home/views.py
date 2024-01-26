from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, Http404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Address
from resturants.models import Restaurant
from foods.models import Food
from django.contrib import messages
from .forms import AddressCreateForm
from accounts.forms import UserInfoUpdateForm


class HomePage(View):
    """
    This is the Basic Class for Handling User MainPage
    """
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'rests': Restaurant.objects.all(),
                'foods': Food.objects.all()
            }
            return render(request, template_name="home.html", context=context)
        else:
            messages.error(request, 'Please Login to use our site.')
            return redirect('account_login_url')


class SettingPage(LoginRequiredMixin, View):
    """
    This is the basic class for showing the setting page.
    """
    def get(self, request):
        context = {
            'user_form': UserInfoUpdateForm(instance=request.user),
            'address_form': AddressCreateForm()
        }
        return render(request, template_name='setting.html', context=context)


class FavPage(LoginRequiredMixin, View):
    """
    This is the View for handling the Favorates Page
    """
    def get(self, request):
        return render(request, template_name='favorite.html')


class FavDelete(LoginRequiredMixin, View):
    """
    This is a class view for managing the user favorites delete.
    """
    def get(self, request, type, item_id):
        user = request.user
        if type == 'restaurant':
            try:
                rest = Restaurant.objects.get(id=item_id)
                user.fav_rest.remove(rest)
            except Restaurant.DoesNotExist:
                messages.error(request, 'Restaurant Not Found!')
                return redirect('fav_page_url')
            messages.success(request, 'Restaurant Removed Successfully!')
            return redirect('fav_page_url')
        elif type == 'Food':
            try:
                food = Food.objects.get(id=item_id)
                user.fav_food.remove(food)
            except Food.DoesNotExist:
                messages.error(request, 'Food Not Found!')
                return redirect('fav_page_url')
            messages.success(request, 'Food Removed Successfully!')
            return redirect('fav_page_url')
        else:
            return Http404(request)


class FavAdd(LoginRequiredMixin, View):
    """
    This is a class view for managing the user favorites add.
    """
    def get(self, request, type, item_id):
        user = request.user
        if type == 'restaurant':
            try:
                rest = Restaurant.objects.get(id=item_id)
                user.fav_rest.add(rest)
            except Restaurant.DoesNotExist:
                messages.error(request, 'Restaurant Not Found!')
                return redirect('fav_page_url')
            messages.success(request, 'Restaurant Added Successfully!')
            return redirect('fav_page_url')
        elif type == 'Food':
            try:
                food = Food.objects.get(id=item_id)
                user.fav_food.add(food)
            except Food.DoesNotExist:
                messages.error(request, 'Food Not Found!')
                return redirect('fav_page_url')
            messages.success(request, 'Food Added Successfully!')
            return redirect('fav_page_url')
        else:
            return Http404(request)


class SavedAddress(LoginRequiredMixin, View):
    """
    This is the View for handling the Saved Addresses
    """
    def get(self, request):
        user = request.user
        fav_addr = user.fav_addr.all()

        context = {
            'fav_addr': fav_addr,
        }

        return render(request, template_name='Fav_Address_Page.html', context=context)


class SavedAddressDelete(LoginRequiredMixin, View):
    """
    This is a class view for managing the user address delete.
    """
    def get(self, request, item_id):
        user = request.user
        try:
            addr = Address.objects.get(id=item_id)
            if user == addr.user:
                addr.delete()
            else:
                return HttpResponseForbidden(request)
        except Address.DoesNotExist:
            messages.error(request, 'Address Not Found!')
            return redirect('setting_page_url')
        messages.success(request, 'Address Removed Successfully!')
        return redirect('setting_page_url')


class SavedAddressAdd(LoginRequiredMixin, View):
    """
    This is a class view for managing the user address delete.
    """
    def post(self, request):
        user = request.user
        form = AddressCreateForm(request.POST)
        if form.is_valid():
            addr = form.instance
            addr.user = user
            addr.save()
            messages.success(request, "The Address Saved Successfully!")
            return redirect('setting_page_url')

        messages.error(request, "The Address is invalid!")
        return redirect('setting_page_url')

    def get(self, request):
        form = AddressCreateForm()
        return render(request, template_name='Temp_Create_Address.html', context={'form': form})

