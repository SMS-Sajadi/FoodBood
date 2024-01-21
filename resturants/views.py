from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Restaurant


class RestaurantDetails(LoginRequiredMixin, DetailView):
    model = Restaurant
    template_name = 'restaurant_detail_page.html'
    context_object_name = 'rest'
    pk_url_kwarg = 'rest_id'
