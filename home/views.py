from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, Http404
from django.views.generic import View
from accounts.models import UserTable
from resturants.models import Restaurant
from foods.models import Food
from django.contrib import messages


class HomePage(View):
    """
    This is the Basic Class for Handling User MainPage
    """
    def get(self, request):
        if request.user.is_authenticated:
            # rests = Restaurant.objects.all()
            # foods = Food.objects.all()
            return render(request, template_name="home_page.html")
        else:
            messages.error(request, 'Please Login to use our site.')
            return redirect('account_login_url')


class SettingPage(View):
    """
    This is the basic class for showing the setting page.
    """
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseForbidden(request)

        return render(request, template_name='Setting_page.html')


class FavPage(View):
    """
    This is the View for handling the Favorates Page
    """
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseForbidden(request)

        user = request.user
        fav_rest = user.fav_rest.all()
        fav_food = user.fav_food.all()

        context = {
            'fav_rest': fav_rest,
            'fav_food': fav_food,
        }

        return render(request, template_name='Fav_Page.html', context=context)


class FavDelete(View):
    """
    This is a class view for managing the user favorites delete.
    """
    def get(self, request, type, item_id):
        if not request.user.is_authenticated:
            return HttpResponseForbidden(request)

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


class FavAdd(View):
    """
    This is a class view for managing the user favorites add.
    """
    def get(self, request, type, item_id):
        if not request.user.is_authenticated:
            return HttpResponseForbidden(request)

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
