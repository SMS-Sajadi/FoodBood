from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Restaurant
from foods.models import Category


class RestaurantDetails(LoginRequiredMixin, DetailView):
    model = Restaurant
    template_name = 'restaurant_detail_page.html'
    context_object_name = 'rest'
    pk_url_kwarg = 'rest_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rest = self.get_object()
        foods = rest.foods.all()
        categs = rest.categories.all()
        context['foods'] = foods
        context['categs'] = categs
        context['active_categ'] = 'All'
        return context


class RestaurantCategoryDetails(LoginRequiredMixin, DetailView):
    model = Restaurant
    template_name = 'restaurant_detail_page.html'
    context_object_name = 'rest'
    pk_url_kwarg = 'rest_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rest = self.get_object()
        category_id = self.kwargs['category_id']
        active_category = Category.objects.get(id=category_id)
        foods = active_category.foods.all()
        categs = rest.categories.all()
        context['foods'] = foods
        context['categs'] = categs
        context['active_categ'] = active_category
        return context
