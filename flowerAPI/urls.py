from django.urls import path, include
import flowerAPI.views as api_view
from django.contrib import admin
from flowerAPI import views
from django.urls import resolve

from rest_framework.routers import DefaultRouter
from rest_framework import routers
from flowerAPI.views import InventoryViewSet



app_name = 'flowerAPI'


router = DefaultRouter()
router.register(r'inventory', InventoryViewSet, basename='inventory')
urlpatterns = router.urls






