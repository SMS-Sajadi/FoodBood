from django.contrib import admin
from .models import Food, Category


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating', 'rest_category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant']
