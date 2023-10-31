from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('',views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),


    path('type/', views.TypeList, name='type'),
    path('type/add/', views.add_type, name='add_type'),
    path('type/<int:type_id>/update/', views.update_type, name='update_type'),
    path('type/delete/<int:type_id>/', views.delete_type, name='delete_type'),


    path('color/', views.ColorList, name='color'),
    path('color/add/', views.add_color, name='add_color'),
    path('color/<int:color_id>/update/', views.update_color, name='update_color'),
    path('color/delete/<int:color_id>/', views.delete_color, name='delete_color'),



    path('inventory/', views.InventoryList, name='inventory'),
    path('inventory/add/', views.add_inventory, name='add_inventory'),
    path('inventory/<int:inventory_id>/update/', views.update_inventory, name='update_inventory'),
    path('inventory/<int:inventory_id>/', views.view_inventory, name='view_inventory'),
    path('inventory/delete/<int:item_id>/', views.delete_inventory, name='delete_inventory'),



    path('customer/', views.CustomerList, name='customer'),
    path('customer/<int:customer_id>/', views.view_customer, name='view_customer'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/<int:customer_id>/update/', views.update_customer, name='update_customer'),
    path('customer/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    

    
]
