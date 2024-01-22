from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrdersList.as_view(), name='orders_list_url'),
    path('<order_id>/add_promo/', views.OrdersAddPromo.as_view(), name='order_add_promo_url'),
    path('add_item/<food_id>/', views.OrderItemAdd.as_view(), name='order_add_item_url'),
    path('delete_item/<orderitem_id>/', views.OrderItemDelete.as_view(), name='order_delete_item_url'),
]
