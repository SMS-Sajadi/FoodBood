from django.urls import path
from . import views


urlpatterns = [
    path('<rest_id>/', views.RestaurantDetails.as_view(), name='restaurant_detail_url'),
    path('<rest_id>/<category_id>/', views.RestaurantCategoryDetails.as_view(), name='restaurant_category_detail_url'),
]
