from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrdersList.as_view(), name='orders_list_url'),
]
