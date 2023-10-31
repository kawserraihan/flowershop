from datetime import timedelta, datetime

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.urls import path

from .models import *

#Register your models here

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name','type','color','price','description', 'image', 'firestore_document_id')
    search_fields = ('name',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','contact','address')
    search_fields = ('name',)



admin.site.register(type, TypeAdmin)
admin.site.register(color, ColorAdmin)
admin.site.register(Inventory,InventoryAdmin)
admin.site.register(Customer, CustomerAdmin)
