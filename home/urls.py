from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page_url'),
    path('favoraites/', views.FavPage.as_view(), name='fav_page_url'),
    path('favoraites/delete/<type>/<item_id>/', views.FavDelete.as_view(), name='fav_delete_url'),
    path('favoraites/add/<type>/<item_id>/', views.FavAdd.as_view(), name='fav_add_url'),
    path('setting/', views.SettingPage.as_view(), name='setting_page_url'),
    path('saved_address/', views.SavedAddress.as_view(), name='saved_address_url'),
    path('saved_address/delete/<item_id>/', views.SavedAddressDelete.as_view(), name='saved_address_delete_url'),
    path('saved_address/add/', views.SavedAddressAdd.as_view(), name='saved_address_add_url'),
    path('order_address_add/', views.OrderAddressAdd.as_view(), name='order_address_add_url'),
]
