from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrdersList.as_view(), name='orders_list_url'),
    path('<order_id>/add_promo/', views.OrdersAddPromo.as_view(), name='order_add_promo_url'),
]
