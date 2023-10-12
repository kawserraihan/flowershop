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
    path('inventory/', views.InventoryList, name='inventory'),
    path('inventory/add/', views.add_inventory, name='add_inventory'),
    path('inventory/<int:inventory_id>/update/', views.update_inventory, name='update_inventory'),
    path('inventory/<int:inventory_id>/', views.view_inventory, name='view_inventory'),
    path('inventory/delete/<int:item_id>/', views.delete_inventory, name='delete_inventory'),
    

    
]
