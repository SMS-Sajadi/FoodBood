from django.urls import path
from . import views


urlpatterns = [
    path('<rest_id>/', views.RestaurantDetails.as_view(), name='restaurant_detail_url'),
]
